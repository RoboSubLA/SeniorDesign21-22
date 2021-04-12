import rospy
import smach
import smach_ros
import time
import threading
from ez_async_data.msg import test
from utilities.comms import Subscriber

# ignore the import error, so far it works
from instrument_tests.test_transitions import testFailedTransition, testPassedTransition
# this state takes the data test from the instrument_tests node and checks whether or not all of
# the tests return true

class State_Zero(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['passed', 'failed'])
        self.zero_sub = Subscriber("instrument_tests", test)

    def execute(self, userdata):
        # for 5 minuts check
        # when we get all posiitive tests (for at least 5 seconds)
        # return state1
        rate = rospy.Rate(1)
        counter = 0
	while counter < 5:
            data = self.zero_sub.get_data()
            rospy.loginfo("imu: " + str(data.imu))
            rospy.loginfo("bar: " + str(data.bar))
            rospy.loginfo("cv: " + str(data.cv))
            rospy.loginfo("dvl: " + str(data.dvl))
            counter = counter + 1
            rate.sleep()
        return testPassedTransition(3)

def main():
    rospy.init_node('state_zero', anonymous=True)
    
    sm = smach.StateMachine(outcomes=['finish'])
    with sm:
        smach.StateMachine.add('SystemCheck', State_Zero(),
                               transitions={'passed': 'finish',
                                            'failed': 'finish'})
    outcome = sm.execute()


if __name__ == '__main__':
    main()


        
