#! /usr/bin/env python
import rospy
from time import sleep
from robosub_messages.msg import Action
from robosub_messages.msg import Barometer, DVL, IMU, Sonar, Hydrophones

class Robosub():
    def __init__(self):
        self.barometer_subscriber =  rospy.Subscriber('barometer_topic', Barometer, self.update, 'barometer')
        self.sonar_subscriber = rospy.Subscriber('sonar_topic', Sonar, self.update, 'sonar')
        self.dvl_subscriber = rospy.Subscriber('dvl_topic', DVL, self.update, 'dvl')
        self.imu_subscriber = rospy.Subscriber('imu_topic', IMU, self.update, 'imu')
        self.hydrophones_subscriber = rospy.Subscriber('hydrophones_topic', Hydrophones, self.update, 'hydrophones')

        self.pitch = 0
        self.yaw = 0
        self.roll = 0
        self.depth = 0
        self.temperature = 0
        self.sonar = 0
        self.hydrophones = 0
        
    def update(self, data, subscriber):
        print(data)
        sleep(1)

if __name__ == '__main__':
    rospy.init_node('robosub_node')
    robosub = Robosub()

    while True:
        print(robosub.pitch)
        sleep(1)

