import smach
import rospy

class TouchBuoy(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','continue','failed'])
    
    def execute(self, userdata):
        transition = 1
        if transition == 1:
            rospy.loginfo("success")
            return 'success'
	if transition == 2:
	    rospy.loginfo("continue")
            return 'continue'
        else:
            rospy.loginfo("failed")
            return 'failed'


def add_ex_buoy_states():
    smach.StateMachine.add('touch_buoy', TouchBuoy(), transitions={'success':'success','continue':'success', 'failed':'reset_for_reattempt'})
    
