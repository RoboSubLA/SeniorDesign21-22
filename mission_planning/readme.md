# Mission Planning
This folder contains everything related to the Mission Planning of the Robosub and will also be it's own ROS package.

## Design
![State Machine Diagram](https://github.com/RoboSubCSULA/SeniorDesign21-22/blob/main/mission_planning/State_Machine.png)

## How it works
... Explain short smach and link to documentation.

### Design
We will use ROS and mainly SMACH to design and create different state machines for the required tasks of the competition.
- State Zero
- Gate State
- Buoy State
- Bins State
- Torpedoes State
- Octagon State
- Pathfinders
- Pingers

### Requirements
- [SMACH](https://wiki.ros.org/smach?distro=melodic)
SMACH is a task-level architecture for rapidly creating complex state machines for robot behavior.
- [Actionlib](http://wiki.ros.org/actionlib)
The actionlib stack provides a standardized interface for interfacing with preemptable tasks.
- [SMACH Viewer](http://wiki.ros.org/smach_viewer)
The smach viewer is a GUI that shows the state of hierarchical SMACH state machines.

## How to work with the code
### Installation

SMACH and actionlib packages are included in ROS, but you need to install smach viewer

1. `cd ~/catkin_ws/src`
2. `git clone https://github.com/ros-visualization/executive_smach_visualization/tree/melodic-devel`
3. `cd ~/catkin_ws`
4. `catkin_make`

### Example Code
#### Creating a state machine
	 class Foo(smach.State):
		 def __init__(self, outcomes=['outcome1', 'outcome2']):
		 # Your state initialization goes here

		 def execute(self, userdata):
		 # Your state execution goes here
			 if xxxx:
				 return 'outcome1'
			 else:
				 return 'outcome2'

#### Adding states to a state machine
	 sm = smach.StateMachine(outcomes=['outcome4','outcome5'])
	 with sm:
		 smach.StateMachine.add('FOO', Foo(),transitions={'outcome1':'BAR',
														  'outcome2':'outcome4'})
		 smach.StateMachine.add('BAR', Bar(),transitions={'outcome2':'FOO'})

#### Creating an introspection Server & using smach viewer
	# First you create a state machine sm
	# .....
	# Creating of state machine sm finished
	# Create and start the introspection server
	sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
	sis.start()
	# Execute the state machine
	outcome = sm.execute()
	# Wait for ctrl-c to stop the application
	rospy.spin()
	sis.stop()

Run the following code after creating a introspection server in a new terminal to view the state of hierarchical SMACH state machines
 `rosrun smach_viewer smach_viewer.py`


### List of Installed Dependencies
#### Packages must be declared if using custom message from the package
- roscpp
- rospy
- std_msgs
- message_generation
- message_runtime
- robosub_messages

### Instrument Test Node Directory
test_instrument_publishers
	starts a rosnode with dummy publishers for all instruments
instrument_monitor
	ROS node dedicated to monitoring all instrument communications
	Publishes custom message
		InstrumentStatus
			bool imu
			bool barometer
	outputs true if there are no issues with instrument outputs and meets expected minimum data rates

## Testing
... How can you test the different states

## The different states
... Explain the function of each state here.

### State Zero
...

### Failed State
...

### Gate State
... In the gate state, the AUV must pass through either side of the gate. For this year's competition, left side of the gate is a G-Man, and the right side of the gate is a Bootlegger. The AUV must pass through one of these gates in order to choose a role. The gate state will position the AUV such that it is pointing at one of these gates. Afterwards, this state will ensure that the AUV is able to pass through one of these gates without any failures or errors. When the AUV has successfull passed through the gate, this state is considered to be a success.

### Buoy State
...

### Bins State
...

### Torpedoes State
...

### Octagon State
...

### Pathfinders
...

### Pingers
...


## What data it publishes
... What data will the ROS package publish.
