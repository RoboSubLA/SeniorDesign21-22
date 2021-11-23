#! /usr/bin/env python
import rospy

from sensors_and_controls.msg import sensors_controls_data

print('Sensors & Controls node started')

print('Publishing data to the topic: sensors_and_controls_data')

while True:
	rospy.init_node('sensors_and_controls')
	publisher = rospy.Publisher('sensors_and_controls_data', sensors_controls_data, queue_size=10)


	rate = rospy.Rate(10)
	data = sensors_controls_data()

	while not rospy.is_shutdown():
        	#DVL dummy data
        	data.DVL_pitch = 20
        	data.DVL_yaw = 15
        	data.DVL_roll = 20
        	data.DVL_x_translation = 10
        	data.DVL_y_translation = 15

        	#IMU dummy data
        	data.IMU_pitch = 0
        	data.IMU_yaw = 10
        	data.IMU_roll = 1

        	#Barometer dummy data
        	data.barometer_depth = 6
        	data.barometer_temperature = 12

        	#Sonar dummy data
        	data.sonar_distance = 8
        	data.sonar_confidence = 0.7

        	#Hydrophones dummy data
		data.hydrophones_direction = 90

        	#Thrusters dummy data
		data.thruster_horisontal_front_left = 1600
        	data.thruster_horisontal_front_right = 1300
        	data.thruster_horisontal_back_left = 1700
        	data.thruster_horisontal_back_right = 1600
        	data.thruster_vertical_front_left = 1600
        	data.thruster_vertical_front_right = 1300
        	data.thruster_vertical_back_left = 1700
        	data.thruster_vertical_back_right = 1600

		publisher.publish(data)
		rate.sleep()

	else:
		exit()
