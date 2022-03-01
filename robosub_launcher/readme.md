# Robosub Launcher

This package is used for launching our Robosub system.

## Launch Files
Overview of the launch files we have, these are located in the `launch` folder. 
### robosub.launcher
This is the launch file to launch the system as normal. 

Currently it will start up the following nodes:

- user_interface
- arduino
- ez_async_data (IMU)

Use the command `roslaunch robosub_launcher robosub.launch` to run this launch file. 

### robosub_dummy.launcher
This is the launch file to launch the system with dummy data from all the sensors.

Currently it will start up the following nodes:

- user_interface
- barometer_dummy
- sonar_dummy
- dvl_dummy
- imu_dummy
- hydrophones_dummy

Use the command `roslaunch robosub_launcher robosub_dummy.launch` to run this launch file. 
