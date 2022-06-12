import smach
import rospy
from utilities.reset_for_reattempt import ResetForReattempt
from utilities.lost_target import LostTarget

class PathMarker(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=['buoy', 'bin', 'failed'])
        with self:
            smach.StateMachine.add('locate_marker', LocateMarker(), transitions={'success': 'align_marker', 'failed': 'reset_for_reattempt'})
            smach.StateMachine.add('align_marker', AlignMarker(), transitions={'success': 'move_forward', 'failed': 'reset_for_reattempt'})
            smach.StateMachine.add('move_forward', MoveForward(), transitions={'buoy': 'buoy', 'bin':'bin', 'failed': 'reset_for_reattempt'})
            smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
            smach.StateMachine.add('reset_for_reattempt', ResetForReattempt(), transitions={'complete':'locate_marker', 'lost_target':'lost_target'})

class LocateMarker(smach.State):
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

class AlignMarker(smach.State):
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

class MoveForward(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['buoy', 'bin', 'failed'])
    
    def execute(self, userdata):
        transition = 1
        if transition == 1:
            rospy.loginfo("buoy")
            return 'buoy'
        if transition == 2:
            rospy.loginfo("bin")
            return 'bin'
        else:
            rospy.loginfo("failed")
            return 'failed'