import smach
import rospy
import time

from ez_async_data.msg import gate
from utilities.comms import Subscriber

class MoveForwardVision(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])
        self.gate_sub = Subscriber('gate', gate)
        # p = rospy.SubscribeListener()
        self.rate = rospy.Rate(5)
        self.elapsedTime = 0
        self.maxTime = 30
		
    def execute(self, userdata):
        beginningTime = time.time()

        while(True):
            self.elapsedTime = time.time()
            data = self.gate_sub.get_data()
            if data.gateseen and data.gatedis < 0.5:
                rospy.loginfo("success")
                return 'success'
            elif (self.elapsedTime - beginningTime) > self.maxTime:
                rospy.loginfo("failed")
                return 'failed'

# Incomplete.
class MoveForwardNoVision(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])
	# self.controls_pub = rospy.Publisher('controls', String, queue_size=10)
	
    def execute(self, userdata):
        # transition = 1
	    # self.controls_pub.publish('go forward')
        return 'success'
        # if transition == 1:
        #     rospy.loginfo("success")
        #     return 'success'
        # elif (beginningTime - self.elapsedTime) < self.maxTime::
        #     rospy.loginfo("failed")
        #     return 'failed'

def add_ex_gate_states():
    smach.StateMachine.add('move_forward_vision', MoveForwardVision(), transitions={'success':'move_forward_no_vision', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('move_forward_no_vision', MoveForwardNoVision(), transitions={'success':'success', 'failed':'reset_for_reattempt'})
