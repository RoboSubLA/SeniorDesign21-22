import rospy
import smach
import smach_ros
import time
import threading
from ez_async_data.msg import test
from utilities.comms import Subscriber

# this state takes the data test from the instrument_tests node and checks whether or not all of
# the tests return true

class State_Zero(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['passed', 'failed'])
        self.zero_sub = Subscriber("instrument_tests", test)

    def execute(self, userdata):
        # for 5 seconds check
        # when we get all posiitive tests (for at least 5 seconds)
        # return state1
        rate = rospy.Rate(1)
        counter = 0
        all_tests_passed = False

	while counter < 5:
            data = self.zero_sub.get_data()
            imu_passed = data.imu
            barometer_passed = data.barometer
            sonar_passed = data.sonar
            hydrophones_passed = data.hydrophones
            cv_passed = data.cv

            rospy.loginfo("imu: " + str(imu_passed))
            rospy.loginfo("barometer: " + str(barometer_passed))
            rospy.loginfo("sonar: " + str(sonar_passed))
            rospy.loginfo("hydrophones: " + str(hydrophones_passed))
            rospy.loginfo("cv: " + str(cv_passed))

            if imu_passed and barometer_passed and sonar_passed and hydrophones_passed and cv_passed:
                all_tests_passed = True
            else:
                all_tests_passed = False
            counter = counter + 1
            rate.sleep()


        if all_tests_passed:
            return 'passed'

        return 'failed' 

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


        
