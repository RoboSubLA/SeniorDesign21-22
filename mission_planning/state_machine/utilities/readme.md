# Utilities
This folder includes some different python files that are useful for the state machine.

## control_interface.py
This file is used to interface with the controls. It has the following functions:

#### getCurrentData()
Get the current data for yaw, roll, pitch & depth
#### publish(setpoints)
Pass in the setpoints that you want to publish

#### isStabilized()
Returns if the Robosub is stabilized or not.

#### setYaw(yaw)
Used to set the yaw of the Robosub

#### setRoll(roll)
Used to set the roll of the Robosub

#### setPitch(pitch)
Used to set the pitch of the Robosub

#### setDepth(depth)
Used to set the depth of the Robosub

#### setDistance(distance)
Used to set the distance of the Robosub

#### bumpIntoBuoy()
Used to get the Robosub to bump into the buoy in the buoy task.

## instrument_monitor.py
This is a node we run to see if we are getting data from all the instruments.

## reset_for_reattempt.py
This is a state that we use for resetting the Robosub if the task goes wrong.

## subscriber.py
This is a class for initializing and interacting with ROS subscribers.

## lost_target.py
This is a state that we use if any of the other states loses its target.
