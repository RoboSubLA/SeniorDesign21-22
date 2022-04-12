#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from robosub_messages.msg import Sonar, Barometer, DVL, IMU, Hydrophones

def callback_hydrophones(data):
    global hydrophones_msg
    hydrophones_msg.direction = data.direction

def callback_imu(data):
    global imu_msg

    imu_msg.roll = data.roll
    imu_msg.yaw = data.yaw
    imu_msg.pitch = data.pitch

def callback_dvl(data):
    global dvl_msg

    dvl_msg.roll = data.roll
    dvl_msg.yaw = data.yaw
    dvl_msg.pitch = data.pitch
    dvl_msg.x_translation = data.x_translation
    dvl_msg.y_translation = data.y_translation

def callback_sonar(data):
    global sonar_msg

    sonar_msg.distance = data.distance
    sonar_msg.confidence = data.confidence

def callback_barometer(data):
    global barometer_msg

    barometer_msg.depth = data.depth
    barometer_msg.temperature = data.temperature

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

while True:
    #Publishers
    sonar_publisher = rospy.Publisher('sonar_topic', Sonar, queue_size=10)
    imu_publisher = rospy.Publisher('imu_topic', IMU, queue_size=10)
    barometer_publisher = rospy.Publisher('barometer_topic', Barometer, queue_size=10)
    dvl_publisher = rospy.Publisher('dvl_topic', DVL, queue_size=10)
    hydrophones_publisher = rospy.Publisher('hydrophones_topic', Hydrophones, queue_size=10)

    #Subscribers
    hydrophones_subscriber = rospy.Subscriber('hydro_new_data', Hydrophones, callback_hydrophones)
    imu_subscriber = rospy.Subscriber('imu_new_data', IMU, callback_imu)
    dvl_subscriber = rospy.Subscriber('dvl_new_data', DVL, callback_dvl)
    sonar_subscriber = rospy.Subscriber('sonar_new_data', Sonar, callback_sonar)
    barometer_subscriber = rospy.Subscriber('barometer_new_data', Barometer, callback_barometer)


    rospy.init_node('dummy_data')
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        sonar_publisher.publish(sonar_msg)
        imu_publisher.publish(imu_msg)
        barometer_publisher.publish(barometer_msg)
        dvl_publisher.publish(dvl_msg)
        hydrophones_publisher.publish(hydrophones_msg)
    	rate.sleep()
