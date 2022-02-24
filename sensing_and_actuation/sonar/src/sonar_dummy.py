#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from sonar.msg import Sonar

while True:
    publisher = rospy.Publisher('sonar_topic', Sonar, queue_size=10)
    rospy.init_node('sonar_dummy')
    rate = rospy.Rate(10)

    sonar_msg = Sonar()
    sonar_msg.distance = 10.52
    sonar_msg.confidence = 0.8

    while not rospy.is_shutdown():
      
        sonar_msg.distance = sonar_msg.distance - 0.1
        time.sleep(2)
        rospy.loginfo(sonar_msg)
        publisher.publish(sonar_msg)
    rate.sleep()