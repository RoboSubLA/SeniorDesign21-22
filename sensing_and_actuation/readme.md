# Sensing And Actuation
This folder contains code for the Sensing and Actuation Node.

You can use `dummydata.py` file for testing purposes.

The sensing and actuation consists of the following sensors and controls:
- DVL
- IMU
- Hydrophones
- Barometer
- Sonar
- 8 Thrusters
- Claw
- Torpedo
- Ball drop

## ROS Node
The name for this ROS node is `sensing_and_actuation`


### Topics

We will have different topics for all the sensors. 

#### Barometer

| barometer_topic                   | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| depth                             | m           | -           | float32   |
| confidence                        | range       |[0-1]        | float32   |

#### Sonar

| sonar_topic                       | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| distance                          | m           | -           | float32   |
| confidence                        | range       |[0-1]        | float32   |

#### DVL

| dvl_topic                         | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| roll                              | degrees     |[0-360       | int32     |
| pitch                             | degrees     |[0-360       | int32     |
| yaw                               | degrees     |[0-360       | int32     |
| x_translation                     | m           |-            | float32   |
| y_translation                     | m           |-            | float32   |

#### IMU

| imu_topic                         | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| roll                              | degrees     |[0-360       | int32     |
| pitch                             | degrees     |[0-360       | int32     |
| yaw                               | degrees     |[0-360       | int32     |

#### Hydrophones

| hydrophones_topic                  | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| direction                         | degrees     |[0-360]      | int32     |
| confidence                        | range       |[0-1]        | float32   |


## Sensors

### Teledyne Pathfinder DVL

#### Will give us following data:

`Pitch(degrees, float)`

`Yaw(degrees, float)`

`Roll(degrees, float)`

`X- Translation(centimeter, float)`

`Y- Translation(centimeter, float)`

[Read more](https://www.eol.ucar.edu/system/files/VN100manual.pdf)

### VectorNav IMU

#### Will give us following data:

`Pitch(degree, float)`

`Yaw(degrees from North, float)`

`Roll(degrees, float)`

### Blue Robotics Bar30 Pressure Sensor
This is a barometer which will give us the depth and temperature the Robosub is operating at.

#### Will give us following data:

`Depth(meters, float)`

`Temperature(celsius, float)`

[Read more](https://github.com/bluerobotics/Bar30-Pressure-Sensor)

### Blue Robotics Ping Sonar

This is a sonar that will detect and give current distance from objects in front of the sonar.

#### Will give us data:

`Distance to Object(millimeters)`

[Read more](https://bluerobotics.com/store/sensors-sonars-cameras/sonar/ping-sonar-r2-rp/)


### AS-1 Hydrophones
This is an array of hydrophones that will listen to to pingers in the pool.

#### Will give us data:

`Pinger Label (string)`

`8-direction (string)`


[Read more](https://www.aquarianaudio.com/as-1-hydrophone.html)

## Actuators

 - Thrusters
 - Torpedo
 - Claw
 - Dropper

 More coming...
