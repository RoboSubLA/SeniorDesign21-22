#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from sonar.msg import Sonar
from barometer.msg import Barometer
from dvl.msg import DVL
from ez_async_data.msg import IMU
from hydrophones.msg import Hydrophones

while True:
    sonar_publisher = rospy.Publisher('sonar_topic', Sonar, queue_size=10)
    imu_publisher = rospy.Publisher('imu_topic', IMU, queue_size=10)
    barometer_publisher = rospy.Publisher('barometer_topic', Barometer, queue_size=10)
    dvl_publisher = rospy.Publisher('dvl_topic', DVL, queue_size=10)
    hydrophones_publisher = rospy.Publisher('hydrophones_topic', Hydrophones, queue_size=10)

    rospy.init_node('dummy_data')
    rate = rospy.Rate(1)

    sonar_msg = Sonar()
    sonar_msg.distance = 10.52
    sonar_msg.confidence = 0.8

    imu_msg = IMU()
    imu_msg.roll = 3.2
    imu_msg.yaw = 0.8
    imu_msg.pitch = 2

    barometer_msg = Barometer()
    barometer_msg.depth = 4
    barometer_msg.temperature = 23

    dvl_msg = DVL()
    dvl_msg.pitch = 3.2
    dvl_msg.yaw = 0.8
    dvl_msg.roll = 1
    dvl_msg.x_translation = 10
    dvl_msg.y_translation = 12
    
    hydrophones_msg = Hydrophones()
    hydrophones_msg.direction = 170
    

    while not rospy.is_shutdown():
        sonar_publisher.publish(sonar_msg)
        imu_publisher.publish(imu_msg)
        barometer_publisher.publish(barometer_msg)
        dvl_publisher.publish(dvl_msg)
        hydrophones_publisher.publish(hydrophones_msg)
    rate.sleep()