import rospy
import smach
import smach_ros
import time
import threading
from utilities.subscriber import Subscriber

# this state takes the data test from the instrument_tests node and checks whether or not all of
# the tests return true

class StateZero(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['passed', 'failed'])
        self.instrument_status = Subscriber("instrument_monitor")

    def execute(self, userdata):
        # for 5 seconds check
        # when we get all posiitive tests (for at least 5 seconds)
        # return state1
        rate = rospy.Rate(1)
        counter = 0
        all_instruments_active = False

        while counter < 5:
            status = self.instrument_status.get_data()
            imu_active = status.imu
            barometer_active = status.barometer
            sonar_active = status.sonar
            hydrophones_active = status.hydrophones
            cv_active = status.cv

            rospy.loginfo("imu: " + str(imu_active))
            rospy.loginfo("barometer: " + str(barometer_active))
            rospy.loginfo("sonar: " + str(sonar_active))
            rospy.loginfo("hydrophones: " + str(hydrophones_active))
            rospy.loginfo("cv: " + str(cv_active))

            if imu_active and barometer_active and sonar_active and hydrophones_active:
                all_instruments_active = True
            else:
                all_instruments_active = False
            counter = counter + 1
            rate.sleep()


            if all_instruments_active:
                return 'passed'

        return 'failed'
