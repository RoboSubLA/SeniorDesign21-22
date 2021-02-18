import rospy
import smach
import smach_ros

#ignore the import error, so far it works
from instrument_tests.test_transitions import testFailedTransition, testPassedTransition


class State_Zero(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['passed','failed'])

    def execute(self, userdata):

        #for 5 minuts check
        #when we get all posiitive tests (for at least 5 seconds)
            #return state1
        return testPassedTransition(3)

        