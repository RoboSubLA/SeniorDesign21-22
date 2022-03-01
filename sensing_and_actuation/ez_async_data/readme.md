# IMU information
This is a ROS Package for our IMU. It's running as a c++ program using Libraries from Vectornav.
The libraries are included in this package in the `cpp` folder.

The Program outputs a custom message message name for import "Rotation"
	composed of

	float32 roll
	float32 pitch
	float32 yaw
    
Topic name is `current_rotation`

## Connecting The IMU
The IMU should be connected with an USB to the computer.
When you have connected the IMU you can find the tty connection that the IMU is connected to with the command `dmesg | grep tty`.

In the `main.cpp` file make the appropriate changes to the SensorPort variable. 

If you want to run the imu node separately you can use the command:

`rosrun ez_async_data ez_async_data`.

## Logging Data From The IMU
Uses `rosbag` data structure to store data that is being published

    
### Storing all topics
Running `rosbag record -a` indicating that all published topics should be accumulated in a bag file.

### Recording a subset of data
`rosbag record -O [filename] [topic1] [topic2]`

The previous commands will make a bagfile in the current directory.



## If permission errors occur

Add user to dialout to allou connections to USB devices. Use the command:

`sudo usermod -a -G dialout $USER`

Make sure to log out and log in toapply the change
