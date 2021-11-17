import smach
import rospy

class MoveForwardVision(smach.State):
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

class MoveForwardNoVision(smach.State):
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

def add_ex_gate_states():
    smach.StateMachine.add('move_forward_vision', MoveForwardVision(), transitions={'success':'move_forward_no_vision', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('move_forward_no_vision', MoveForwardNoVision(), transitions={'success':'success', 'failed':'reset_for_reattempt'})
