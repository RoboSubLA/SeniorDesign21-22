# Sensing And Actuation
This folder contains code for all the sensors and actuators.

## Folders
In the `src` folder you can find these folders for our different sensors:

### [arduino](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/sensing_and_actuation/src/arduino)
This folder contains the Arduino code. It will have the barometer and sonar attached to it.


### [imu](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/sensing_and_actuation/src/imu)
This folder contains the code for connecting to and getting data from the imu. This is written in c++.

To run the imu use the command: `rosrun sensing_and_actuation imu`

### [dvl](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/sensing_and_actuation/src/dvl)
This node contains the code for connecting to and getting data from the dvl

### [hydrophones](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/sensing_and_actuation/src/hydrophones)
This node contains the code for connecting to and getting data from the hydrophones

### [dummy_data](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/sensing_and_actuation/src/dummy_data)
The code in this folder is used for publishing dummy data for all the sensors.

To run the dummy_data node use the command `rosrun sensing_and_actuation dummy_data_main.py`

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


## To be continued

 - Thrusters
 - Torpedo
 - Claw
 - Dropper
