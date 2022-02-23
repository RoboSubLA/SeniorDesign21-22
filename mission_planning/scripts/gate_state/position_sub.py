import smach
import rospy

from std_msgs.msg import String
from ez_async_data.msg import CV
from utilities.comms import Subscriber

import time

#CV
#targetSeen, targetDis, xOffset, yOffset 

class PositionSub(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success', 'failed', 'timeout'])
        self.gate_sub = Subscriber('cv_data', CV)
        self.controls_pub = rospy.Publisher('controls', String, queue_size=10)
        # p = rospy.SubscribeListener()
        self.rate = rospy.Rate(5)
        self.elapsedTime = 0
        self.maxTime = 30
        self.xError = 10
        self.yError = 10


    def execute(self, userdata):
        output = ''
		beginningTime = time.time()
        while(True):
            self.elapsedTime = time.time()
            if (beginningTime - self.elapsedTime) < self.maxTime:
                return('timeout')

            # Get data from CV.
            data = self.gate_sub.get_data()
            
            if data.xOffset < self.xError and data.yOffset < self.yError:
                return 'success'
        
            command = self.getCenterCommand(data)
            self.controls_pub.publish(command[0] + '\n'+ command[1] + '/n/n')

            output += 'Target Seen: ' + str(data.targetSeen) + '\n'
            output += 'Target Dis: ' + str(data.targetDis) + '\n'
            output += 'xOffset: ' + str(data.xOffset) + '\n'
            output += 'yOffset: ' + str(data.yOffset) + '\n\n'
            rospy.loginfo(output)
            self.rate.sleep()

    def getCenterCommand(self, data):
        setpoints = []
        if data.xOffset > self.xError:
            # The AUV is too far right to pass through the gate. The x value has to be decreased, so a command is sent to Controls to move left, or decrease x.
            setpoint.append('go left')
        elif data.xOffset < -self.xError:
            # The AUV is too far left to pass through the gate. The x value has to be increased, so a command is sent to Controls to move right, or increase x.
            setpoint.append('go right')

        if data.yOffset > self.yError:
            # The AUV is too high to pass through the gate. Height has to be decreased, so a command is sent to Controls to decrease height.
            setpoint.append('go down')
        elif data.yOffset < -self.yError:
            # The AUV is too low to pass through the gate. Height has to be increased, so a command is sent to Controls to increase height.
            setpoint.append('go up')
		return setpoints
