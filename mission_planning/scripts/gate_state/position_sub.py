import smach
import rospy
import time

from std_msgs.msg import String
from ez_async_data.msg import CV
from utilities.comms import Subscriber
from dvl.msg import DVL
from sonar.msg import Sonar

#CV
#targetSeen, targetDis, xOffset, yOffset 

class PositionSub(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success', 'no_target', 'timeout'])
        self.gate_sub = Subscriber('cv_data', CV)
        self.sonar_test_sub =  Subscriber("sonar_topic", Sonar)
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
			# Get data from CV.
            data = self.gate_sub.get_data()
            data1 = self.sonar_test_sub.get_data()
            
            if (self.elapsedTime - beginningTime) > self.maxTime:
                if data.targetSeen:
                    return('timeout')
                else:
                    return('no_target')
				
            if data.xOffset < self.xError and data.yOffset < self.yError and data.targetSeen:
                    return 'success'
        
            command = self.getCenterCommand(data)
            self.controls_pub.publish(command[0] + '\n'+ command[1] + '/n/n')

            output += 'Target Seen: ' + str(data.targetSeen) + '\n'
            output += 'Target Dis: ' + str(data.targetDis) + '\n'
            output += 'xOffset: ' + str(data.xOffset) + '\n'
            output += 'yOffset: ' + str(data.yOffset) + '\n\n'
            #(TEMPORARY) For debugging and testing.
            output += 'Distance: ' + str(data1.distance) + '\n'
            output += 'Time: ' + str(self.elapsedTime - beginningTime) + '\n'
            rospy.loginfo(output)
            self.rate.sleep()

    def getCenterCommand(self, data):
        setpoints = []
        if data.xOffset > self.xError:
			# The AUV is too far right to pass through the gate. The x value has to be decreased, so a command is sent to Controls to move left, or decrease x.
            setpoints.append('go left')
        elif data.xOffset < -self.xError:
			# The AUV is too far left to pass through the gate. The x value has to be increased, so a command is sent to Controls to move right, or increase x.
            setpoints.append('go right')
        else:
            setpoints.append('N/A')

        if data.yOffset > self.yError:
			# The AUV is too high to pass through the gate. Height has to be decreased, so a command is sent to Controls to decrease height.
            setpoints.append('go down')
        elif data.yOffset < -self.yError:
			# The AUV is too low to pass through the gate. Height has to be increased, so a command is sent to Controls to increase height.
            setpoints.append('go up')
        else:
            setpoints.append('N/A')
        return setpoints
