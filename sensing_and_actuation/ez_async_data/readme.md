# IMU information
This is a ROS Package for our IMU. It's running as a c++ program using Libraries from Vectornav.
The libraries are included in this package in the `cpp` folder.

The Program outputs a custom message message name for import "Rotation"
	composed of

		`float32 roll`
		`float32 pitch`
		`float32 yaw`
    
Topic name is `current_rotation`

        
## IMU LOGS
Uses `rosbag` data structure to store data that is being published

    
### Storing all topics
Running `rosbag record -a` indicating that all published topics should be accumulated in a bag file.

### Recording a subset of data
`rosbag record -O [filename] [topic1] [topic2]`

The previous commands will make a bagfile in the current directory.


# Getting the IMU working
1. Find the tty connection the vectornav is connected to. You can use the command `dmesg | grep tty`
2. Make appropriate changed to the device name in the src/main.cpp file

## If permission errors occur

Add user to dialout to allou connections to USB devices. Use the command:

`sudo usermod -a -G dialout $USER`

Make sure to log out and log in toapply the change
