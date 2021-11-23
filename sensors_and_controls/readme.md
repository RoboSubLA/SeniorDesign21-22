# Sensors And Controls
This folder contains code for the Sensing and Controls Node.

You can use `dummydata.py` file for testing purposes.

## ROS Node
The name for this ROS node is `sensors_and_controls`


#### Publishing

It will publish an msg with the following data to the topic `sensors_and_controls_data`

| Sensor/Control                    | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| DVL_pitch                         | degrees     | -           | float     |
| DVL_yaw                           | degrees     | -           | float     |
| DVL_roll                          | degrees     | -           | float     |
| DVL_x_translation                 | millimeters | -           | float     |
| DVL_y_translation                 | millimeters | -           | float     |
| IMU_pitch                         | degrees     | -           | float     |
| IMU_yaw                           | degrees     | -           | float     |
| IMU_roll                          | degrees     | -           | float     |
| barometer_depth                   | meters      | -           | float     |
| barometer_temperature             | celsius     | -           | float     |
| sonar_distance                    | meters      | -           | float     |
| sonar_confidence                  | percentage  | [0-1]       | float     |
| hydrophones_direction             | degrees     | -           | float     |
| thruster_horisontal_front_left    | power       | -           | float     |
| thruster_horisontal_front_right   | power       | -           | float     |
| thruster_horisontal_back_left     | power       | -           | float     |
| thruster_horisontal_back_right    | power       | -           | float     |
| thruster_vertical_front_left      | power       | -           | float     |
| thruster_vertical_front_right     | power       | -           | float     |
| thruster_vertical_back_left       | power       | -           | float     |
| thruster_vertical_back_right      | power       | -           | float     |


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

[Read more](https://www.aquarianaudio.com/as-1-hydrophone.html)

## Controls

 - Thrusters
 - Torpedo
 - Claw
 - Dropper

 More coming...
