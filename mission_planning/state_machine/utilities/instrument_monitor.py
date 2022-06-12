#!/usr/bin/env python2

import rospy
import time
from robosub_messages.msg import Barometer, Sonar, DVL, IMU, Hydrophones, CV, InstrumentMonitor
from subscriber import Subscriber

instrument_monitor = InstrumentMonitor()
instrument_monitor.imu = False
instrument_monitor.barometer = False
instrument_monitor.cv = False
instrument_monitor.dvl = False
instrument_monitor.hydrophones = False
instrument_monitor.sonar = False

imu_time = 0
dvl_time = 0
cv_time = 0
barometer_time = 0
hydrophones_time = 0
sonar_time = 0


def main():
    rospy.init_node('tester', anonymous=True)
    rate = rospy.Rate(50)
    barometer_subscriber = Subscriber('barometer_topic')
    sonar_subscriber = Subscriber('sonar_topic')
    imu_subscriber = Subscriber('imu_topic')
    dvl_subscriber = Subscriber('dvl_topic')
    hydrophones_subscriber = Subscriber('hydrophones_topic')

    publisher = rospy.Publisher("instrument_monitor", InstrumentMonitor, queue_size=10)

    while not rospy.is_shutdown():
        instrument_monitor.barometer = barometer_subscriber.is_active()
        instrument_monitor.sonar = sonar_subscriber.is_active()
        instrument_monitor.imu = imu_subscriber.is_active()
        instrument_monitor.dvl = dvl_subscriber.is_active()
        instrument_monitor.hydrophones = hydrophones_subscriber.is_active()

        publisher.publish(instrument_monitor)
        rate.sleep()
        # rospy.spin()



if __name__ == '__main__':
    main()
   
