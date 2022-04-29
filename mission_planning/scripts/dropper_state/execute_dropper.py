import smach
import rospy

class CheckContainer(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['open','closed','failed'])
    
    def execute(self, userdata):
        transition = 2
        if transition == 1:
            rospy.loginfo("open")
            return 'open'
	if transition == 2:
	    rospy.loginfo("closed")
            return 'closed'
        else:
            rospy.loginfo("failed")
            return 'failed'

class OpenContainer(smach.State):
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

class PickUp(smach.State):
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

class Surface(smach.State):
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


def add_ex_dropper_states():
    smach.StateMachine.add('check_container', CheckContainer(), transitions={'open':'pick_up','closed':'open_container', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('open_container', OpenContainer(), transitions={'continue':'pick_up', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('pick_up', PickUp(), transitions={'continue':'surface', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('surface', Surface(), transitions={'success':'success', 'failed':'reset_for_reattempt'})
    
