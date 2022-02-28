# Arduino Package
This ROS package is for connecting with the Arduino board we are using. We're using a Arduino Mega 2560 Board.

## Setting up the Arduino

The Arduino should be connected to the computer through an usb cable.

You can run the command `ls /dev/ttyACM0` to check if the Arduino is connected.

#### 1. Installing Libraries
In your terminal run the commands:

> sudo apt-get install ros-melodic-rosserial-arduino`
>
> sudo apt-get install ros-melodic-rosserial`

#### 2. Building All Packages
When those libraries are installed you want to cd into your workspace and run:

> catkin_make
>
> catkin_make install

#### 3. Make ros_lib Library
Locate and cd into your Arduino libraries folder. Example: `cd ~/Arduino/libraries`

Then run:  

> rm -rf ros_lib
>
> rosrun rosserial_arduino make_libraries.py .

This will install the  `ros_lib` library for you. This step will have to be repeated every time you update any of the other packages the `arduino_node` depends on.

#### 4. In Your Code
In your code include the line

    #include <ros.h>

At the start of your program to import the library. 



#### Documentation  
[Read more about setting up your Arduino IDE](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup)

## Connecting The Barometer
#### Hardware
The barometer is connected to the Arduino through 4 wires.

- Power (Red)
- Ground (Black)
- SDA (White)
- SCL (Green)


#### Software
Install the library `BlueRobotics MS5837 Library`.

[Documentation for the library](https://github.com/bluerobotics/BlueRobotics_MS5837_Library)
