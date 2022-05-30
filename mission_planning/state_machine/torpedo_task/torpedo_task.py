import smach
import rospy
from utilities.reset_for_reattempt import ResetForReattempt
from utilities.lost_target import LostTarget

class TorpedoTask(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=['success','failed'])
        with self:
            smach.StateMachine.add('position_sub', PositionSub(), transitions={'success': 'shoot_heart', 'failed': 'reset_for_reattempt'})
            smach.StateMachine.add('shoot_heart', ShootHeart(), transitions={'success': 'success', 'failed': 'reset_for_reattempt'})
            smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
            smach.StateMachine.add('reset_for_reattempt', ResetForReattempt(), transitions={'complete':'position_sub', 'lost_target':'lost_target'})
     
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

class ShootHeart(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success', 'failed'])
    
    def execute(self, userdata):
        transition = 1
        if transition == 1:
            rospy.loginfo("success")
            return 'success'
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