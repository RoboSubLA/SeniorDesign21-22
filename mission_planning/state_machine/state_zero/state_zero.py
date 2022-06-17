import rospy
import smach
import smach_ros
import time
import threading
from utilities.subscriber import Subscriber
from utilities.control_interface import ControlInterface

# this state takes the data test from the instrument_tests node and checks whether or not all of
# the tests return true

class StateZero(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['passed', 'failed'])
        self.control_interface = ControlInterface()

    def execute(self, userdata):
        # for 5 seconds check
        # when we get all posiitive tests (for at least 5 seconds)
        # return state1
        if control_interface.isInstrumentsConnected():
            return 'passed'
        else:
            return 'failed'
