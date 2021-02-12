import rospy
import smach
import smach_ros

#ignore the import error, so far it works
from instrument_tests.test_transitions import testFailedTransition, testPassedTransition


class State_Zero(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['passed','failed'])

    def execute(self, userdata):

        #insert all test methods here

        # return testFailedTransition(3)
        return testPassedTransition(3)

        #rough idea of how tests will be executed
        # if all tests passed:
        #     return 'passed'

        #triggers after predetermined amount of time
        # if testTimeout():
        #     return 'failed'