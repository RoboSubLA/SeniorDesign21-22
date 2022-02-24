#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from barometer.msg import Barometer

while True:
    publisher = rospy.Publisher('barometer_topic', Barometer, queue_size=10)
    rospy.init_node('barometer_dummy')
    rate = rospy.Rate(10)

    barometer_msg = Barometer()
    barometer_msg.depth = 3.2
    barometer_msg.confidence = 0.8

    while not rospy.is_shutdown():
      
        barometer_msg.depth = barometer_msg.depth + 0.1
        time.sleep(2)
        rospy.loginfo(barometer_msg)
        publisher.publish(barometer_msg)
    rate.sleep()