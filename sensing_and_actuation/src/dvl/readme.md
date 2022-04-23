# DVL
This is the package for the dvl. The dvl we are using is [Teledyne Pathfinder DVL](https://www.eol.ucar.edu/system/files/VN100manual.pdf)

### Will give us following data:

`Pitch(degrees, float)`

`Yaw(degrees, float)`

`Roll(degrees, float)`

`X- Translation(centimeter, float)`

`Y- Translation(centimeter, float)`

| dvl_topic                         | Metric      | Range       | Type      |
| ----------------------------------| ----------- |-----------  | ----------|
| roll                              | degrees     |[0-360]      | int32     |
| pitch                             | degrees     |[0-360]      | int32     |
| yaw                               | degrees     |[0-360]      | int32     |
| x_translation                     | m           |-            | float32   |
| y_translation                     | m           |-            | float32   |

### Notes from last year

Testing the DVL
CR1
ck
PS0


Deployment test
pa


so far
pa test passed
connection - passes, finnicky



dvl_test.py
	has coded the pt5 and pa tests
	no changes to any data
	unsure what the problems are
