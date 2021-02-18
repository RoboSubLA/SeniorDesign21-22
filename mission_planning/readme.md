# dependencies when creating the package
	required for each new package with custom
	published message

# instrument test node directory
test_instrument_publishers
	starts a rosnode with dummy publishers for all instruments
instrument_monitor
	ROS node dedicated to monitoring all instrument communications
	Publishes custom message
		InstrumentStatus
			bool imu
			bool barometer
	outputs true if there are no issues with instrument outputs and meets expected minimum data rates

# list of dependencies currentyl installed
### packages must be declared if using custom message from the package
roscpp
rospy
std_msgs
message_generation
message_runtime
ez_async_data (imu package)