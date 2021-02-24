#!/usr/bin/env python
import rospy
from computer_vision.msg import Cv_data
"""
    BY: AREN PETROSSIAN 
"""
def the_logger(the_data):
   print(the_data)

def the_listener():
   rospy.init_node('the_subscriber', anonymous=True)
   rospy.Subscriber('cv_pub', Cv_data, the_logger)
   rospy.spin() 

if __name__ == '__main__': 
   the_listener()