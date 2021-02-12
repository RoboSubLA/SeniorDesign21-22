

#runs the tests for all subsystems

import roslib
import rospy
import smach
import smach_ros


class SystemCheck(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['passed', 'failed']

    def execute(self, userdata):
        
        checkState(checkBaromete)
        checkState(checkIMU)
        checkState(checkCV)
        


    #after 30 seconds if not passed send fail state
            pass
        while !checkIMU():
            pass
            #checkImu()
            #checkCV()
            #checkDVL()
            #testThrusters()
            #check/testNav()


    def checkState(function):
        while !function():
            #after 30 seconds if not passed send failed state
            pass
