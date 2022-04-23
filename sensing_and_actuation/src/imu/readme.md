# IMU
This is the folder containing code for our IMU. The IMU we are using is VectorNav IMU.
It's running as a c++ program using Libraries from Vectornav.
The libraries are included in the `cpp` folder.

### Will give us following data:

`Pitch(degrees, float)`

`Yaw(degrees from North, float)`

`Roll(degrees, float)`

| imu_topic                         | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| roll                              | degrees     |[0-360]      | int32     |
| pitch                             | degrees     |[0-360]      | int32     |
| yaw                               | degrees     |[0-360]      | int32     |


## Connecting The IMU
The IMU should be connected with an USB to the computer.
When you have connected the IMU you can find the tty connection that the IMU is connected to with the command `dmesg | grep tty`.

In the `main.cpp` file make the appropriate changes to the SensorPort variable.

If you want to run the imu node separately you can use the command:

`rosrun sensing_and_actuation imu`.

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
