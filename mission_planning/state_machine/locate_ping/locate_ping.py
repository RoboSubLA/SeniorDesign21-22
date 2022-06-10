import smach
import rospy
from utilities import Subscriber

class LocatePing(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=['torpedo', 'octagon', 'failed'])
        with self:
            smach.StateMachine.add('find_direction', FindDirection(), transitions={'success': 'move_forward', 'failed': 'failed'})
            smach.StateMachine.add('move_forward', MoveForward(), transitions={'torpedo': 'torpedo', 'octagon': 'octagon', 'failed': 'find_direction'})

class FindDirection(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])
    
    def execute(self, userdata):
        #Subscribe to hydrophones and find direction.
        hydrophones_subscriber = Subscriber('hydrophones_topic')
        #Turn the sub in the right direction by adjusting the yaw. Then continue to Move Forward state
        transition = 1
        if transition == 1:
            rospy.loginfo("success")
            return 'success'
        else:
            rospy.loginfo("failed")
            return 'failed'

class MoveForward(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['torpedo', 'octagon', 'failed'])
    
    def execute(self, userdata):
        transition = 1
        if transition == 1:
            rospy.loginfo("torpedo")
            return 'torpedo'
        if transition == 2:
            rospy.loginfo("octagon")
            return 'octagon'
        else:
            rospy.loginfo("failed")
            return 'failed'