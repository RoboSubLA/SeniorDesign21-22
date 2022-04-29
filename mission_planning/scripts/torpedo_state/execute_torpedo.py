import smach
import rospy

class ShootHeart(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['open','lever','failed'])
    
    def execute(self, userdata):
        transition = 2
        if transition == 1:
            rospy.loginfo("open")
            return 'open'
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

class ShootHead(smach.State):
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


def add_ex_torpedo_states():
    smach.StateMachine.add('shoot_heart', ShootHeart(), transitions={'open':'shoot_head','lever':'pull_lever', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('pull_lever', PullLever(), transitions={'continue':'shoot_head', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('shoot_head', ShootHead(), transitions={'success':'success', 'failed':'reset_for_reattempt'})
    
