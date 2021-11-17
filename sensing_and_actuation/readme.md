# Sensing and Actuation

This node is where all our sensor and controls will be connected.

It consists of an Arduino program with a ROS node on it where all the sensors and controls are connected. In the arduino program we will have functions for translating the data we get into useful information that we will publish for the rest of the Robosub system. The program will also interface with the controls and listen for commands given by the other nodes in the system. 

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
This is a barometer which will give us the depth of the Robosub.

#### Will give us following data:

`Depth(meters, float)`

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
