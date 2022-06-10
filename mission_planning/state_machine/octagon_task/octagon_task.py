import smach
import rospy
from utilities.reset_for_reattempt import ResetForReattempt
from utilities.lost_target import LostTarget

# State machine for the gate task.
class OctagonTask(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=['success','failed'])
        with self:
            smach.StateMachine.add('position_sub', PositionSub(), transitions={'success': 'success', 'failed': 'reset_for_reattempt'})
            smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
            smach.StateMachine.add('reset_for_reattempt', ResetForReattempt(), transitions={'complete':'position_sub', 'lost_target':'lost_target'})
      
# Add different sub states under here.
class PositionSub(smach.State):
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

