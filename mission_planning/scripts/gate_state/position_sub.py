import smach
import rospy

#lines for importing outside of current directory
import sys

class PositionSub(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])
        gate_sub = rospy.Subscriber()
        controls = rospy.Publisher()
        # p = rospy.SubscribeListener()  
    def execute(self, userdata):
        #get data from CV concerning gate
        pass
