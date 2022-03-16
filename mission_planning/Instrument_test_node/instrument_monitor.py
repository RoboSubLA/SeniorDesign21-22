#!/usr/bin/env python2

import rospy
import time
from barometer.msg import Barometer 
from sonar.msg import Sonar
from dvl.msg import DVL
from ez_async_data.msg import IMU, test, Rotation, CV
from hydrophones.msg import Hydrophones
from std_msgs.msg import String

instrument_test = test()
instrument_test.imu = False
instrument_test.barometer = False
instrument_test.cv = False
instrument_test.dvl = False
imuDataTime = 0
dvlDataTime = 0
cvDataTime = 0
barometerDataTime = 0


def imu_callback(data):
    global imuDataTime
    imuDataTime = time.time()
    instrument_test.imu = True
    rospy.loginfo("Pitch: %d, Yaw: %d, Roll: %d", data.pitch, data.yaw, data.roll)


def dvl_callback(data):
    global dvlDataTime
    dvlDataTime = time.time()
    instrument_test.dvl = True
    rospy.loginfo('dvl: ' + str(data))


def cv_callback(data):
    global cvDataTime
    cvDataTime = time.time()
    instrument_test.cv = True
    rospy.loginfo("targetSeen: %d, targetDis: %d, targetdiscenter: %d",
                  data.targetSeen, data.targetDis, data.targetdiscenter)


def barometer_callback(data):
    # barometer data should register the average atm of a standard swimming pool (~700 - 770)
    global barometerDataTime
    barometerDataTime = time.time()
    instrument_test.barometer = True
    rospy.loginfo('Barometer: ' + str(data.depth) + ' depth')


def main():
    rospy.init_node('tester', anonymous=True)
    rate = rospy.Rate(50)

    rospy.Subscriber("imu_topic", Rotation, imu_callback)
    rospy.Subscriber("cv_data", CV, cv_callback)
    rospy.Subscriber("barometer_topic", Barometer, barometer_callback)
    rospy.Subscriber("dvl_topic", DVL, dvl_callback)
    pub = rospy.Publisher("instrument_tests", test, queue_size=10)

    while not rospy.is_shutdown():
        if time.time() - imuDataTime >= .1:
            instrument_test.imu = False
        if time.time() - dvlDataTime >= .1:
            instrument_test.dvl = False
        if time.time() - cvDataTime >= .1:
            instrument_test.cv = False
        if time.time() - barometerDataTime >= .1:
            instrument_test.barometer = False
        pub.publish(instrument_test)
        rate.sleep()
        # rospy.spin()



if __name__ == '__main__':
    main()
    # make pub
    # wait for data
    # if vaild return true
    # else false
