# Sensing And Actuation
This folder contains code for all the sensors and actuators. 

## Nodes
In the `src` folder you can find these different nodes:

### arduino
This nodes contain the arduino code. It will have the barometer and sonar attached to it.

### imu
This node contains the code for connecting to and getting data from the imu. This is written in c++.

### dvl
This node contains the code for connecting to and getting data from the dvl

### hydrophones
This node contains the code for connecting to and getting data from the hydrophones

### dummy_data
You can run this node and will publish dummy data for all the sensors. It also provides a user interface to alter the data it publishes. 


## hydrophones
This is our package for the hydrophones. It's using [AS-1 Hydrophones](https://www.aquarianaudio.com/as-1-hydrophone.html).

### Will give us data:

`Pinger Label (string)`

`8-direction (string)`

### Topic
| hydrophones_topic                 | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| direction                         | degrees     |[0-360]      | int32     |
| confidence                        | range       |[0-1]        | float32   |



## barometer

### Blue Robotics Bar30 Pressure Sensor
This is a barometer which will give us the depth and temperature the Robosub is operating at. The barometer we are using is [Blue Robotics Bar30 Pressure Sensor](https://github.com/bluerobotics/Bar30-Pressure-Sensor)

### Will give us following data:

`Depth(meters, float)`

`Temperature(celsius, float)`

### Topic
| barometer_topic                   | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| depth                             | m           | -           | float32   |
| temperature                       | Celcius     | -           | float32   |


## sonar

This is a sonar that will detect and give current distance from objects in front of the sonar. The sonar we are using is [Blue Robotics Ping Sonar](https://bluerobotics.com/store/sensors-sonars-cameras/sonar/ping-sonar-r2-rp/)

### Will give us data:

`Distance to Object(millimeters)`

### Topic
| sonar_topic                       | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| distance                          | m           | -           | float32   |
| confidence                        | range       |[0-1]        | float32   |


## dvl
This is the package for the dvl. The dvl we are using is [Teledyne Pathfinder DVL](https://www.eol.ucar.edu/system/files/VN100manual.pdf)

### Will give us following data:

`Pitch(degrees, float)`

`Yaw(degrees, float)`

`Roll(degrees, float)`

`X- Translation(centimeter, float)`

`Y- Translation(centimeter, float)`

### Topic

| dvl_topic                         | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| roll                              | degrees     |[0-360]      | int32     |
| pitch                             | degrees     |[0-360]      | int32     |
| yaw                               | degrees     |[0-360]      | int32     |
| x_translation                     | m           |-            | float32   |
| y_translation                     | m           |-            | float32   |


## imu
This is the package for our IMU. The IMU we are using is VectorNav IMU.

### Will give us following data:

`Pitch(degrees, float)`

`Yaw(degrees from North, float)`

`Roll(degrees, float)`


### Topic

| imu_topic                         | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| roll                              | degrees     |[0-360]      | int32     |
| pitch                             | degrees     |[0-360]      | int32     |
| yaw                               | degrees     |[0-360]      | int32     |


## To be continued

 - Thrusters
 - Torpedo
 - Claw
 - Dropper
