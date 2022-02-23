#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from ez_async_data.msg import IMU

while True:
    publisher = rospy.Publisher('imu_dummy_topic', IMU, queue_size=10)
    rospy.init_node('imu_dummy')
    rate = rospy.Rate(10)

    imu_msg = IMU()
    imu_msg.roll = 3.2
    imu_msg.yaw = 0.8
    imu_msg.pitch = 2

    while not rospy.is_shutdown():
      
        time.sleep(2)
        rospy.loginfo(imu_msg)
        publisher.publish(imu_msg)
    rate.sleep()