import smach
import smach_ros
import rospy

from std_msgs.msg import String
from robosub_messages.msg import CV
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
        #get data from CV concerning gate
        
        output = ''
        while(True):
            # self.elapsedTime = time.time()
            # if self.elapsedTime > self.maxTime:
            #     return('timeout')

            #get current data
            data = self.gate_sub.get_data()
            
            if data.xOffset < self.xError and data.yOffset < self.yError:
                #send controls current heading, current depth, as setpoints
                return 'success'
        
            command = self.getCenterCommand()
            self.controls_pub.publish(command[0] + '\n'+ command[1] + '/n/n')

            output += 'Target Seen: ' + str(data.targetSeen) + '\n'
            output += 'Target Dis: ' + str(data.targetDis) + '\n'
            output += 'xOffset: ' + str(data.xOffset) + '\n'
            output += 'yOffset: ' + str(data.yOffset) + '\n\n'
            rospy.loginfo(output)
            self.rate.sleep()

    def getCenterCommand():
        setpoints = []
        if x > xError:
            #need to increase height
            #send to controls height increase command
            setpoint.append('go up')

        elif x < -xError:
            #need to decrease height
            #send to controls decrease height command
            setpoint.append('go down')

        if y > yError:
            #need to increase height
            #send to controls height increase command
            setpoint.append('go left')

        elif y < -yError:
            #need to decrease height
            #send to controls decrease height command
            setpoint.append('go down')


