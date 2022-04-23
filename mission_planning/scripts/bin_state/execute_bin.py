import smach
import rospy

class CheckBins(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','lever','failed'])
    
    def execute(self, userdata):
        transition = 2
        if transition == 1:
            rospy.loginfo("success")
            return 'success'
	if transition == 2:
	    rospy.loginfo("lever")
            return 'lever'
        else:
            rospy.loginfo("failed")
            return 'failed'

class PullLever(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['continue','failed'])
    
    def execute(self, userdata):
        transition = 1
        if transition == 1:
            rospy.loginfo("success")
            return 'continue'
        else:
            rospy.loginfo("failed")
            return 'failed'

class DropObject(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])
    
    def execute(self, userdata):
        transition = 1
        if transition == 1:
            rospy.loginfo("success")
            return 'success'
        else:
            rospy.loginfo("failed")
            return 'failed'


def add_ex_bin_states():
    smach.StateMachine.add('check_bins', CheckBins(), transitions={'success':'drop_object','lever':'pull_lever', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('pull_lever', PullLever(), transitions={'continue':'drop_object', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('drop_object', DropObject(), transitions={'success':'success', 'failed':'reset_for_reattempt'})
    
