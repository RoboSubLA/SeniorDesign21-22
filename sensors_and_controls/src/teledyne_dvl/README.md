# Teledyne DVL
This folder contains files and code related to the Teledyne Pathfinder DVL.

The DVL will be connected to the computer and will directly communicate with the computer equivalent.

`dvl_dummy.ino` is currently used to create fake dummy data to be send using an arduino. `dvl_dummy.ino` is used to create and send dummy data using `serial`. If using `dvl_dummy.ino` to create fake dummy data then change the argument in `main.py` to `/dev/ttyACM0` otherwise keep as `COM4` to communicate with the DVL.

`dvl_driver.py` has yet to be tested with the Pathfinder DVL. Currently used to receive dummy data and print it out.

The `main.py` file is to be used to run start things up.
Change the port in `main.py` if necessary if you cannot connect to the current port.

In the `main.py` file import either dvl_driver.py as DVL or dvl_test.py as DVL for testing purposes.

## Getting Started
### Requirements:
- Python 2.7
- Ros Melodic
- Ubuntu 18.04
- Possibly [rosserial](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup)

### To run the code
- Go to root folder of project
- `catkin_make`
- `source devel/setup.bash`
- `rosrun sensing_and_actuation main.py`