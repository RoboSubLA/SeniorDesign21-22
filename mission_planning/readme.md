# Mission Planning
This folder contains everything related to the Mission Planning of the Robosub and will also be it's own ROS package.

## How it works
... Explain short smach and link to documentation.

## How to work with the code
... How can a new developer start working with the code

## Testing
... How can you test the different states

## The different states
... Explain the function of each state here.

### State Zero
...

### Failed State
...

### Buoy State
...

### Gate State

...


## What data it publishes
... What data will the ROS package publish.


# This is the info from the previous year might be useful for when updating the documentation

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
