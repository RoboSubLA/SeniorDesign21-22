# Sensing and Actuation

This node is where all our sensor and controls will be connected.

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

Will give us following data:

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

## controls

 - Thrusters
 - Cooling pump
 - Torpedo
 - Claw
 - Dropper

 More coming...
