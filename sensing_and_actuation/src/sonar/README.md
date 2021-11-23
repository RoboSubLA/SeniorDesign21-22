mega-sonar.ino - This code only works with Arduino Mega, runs off Arduino IDE and serial monitor, check code for Rx,Tx pin placement


sonarROS.ino - ran on Ubuntu 20.04, and ROS noetic 

Ping sonar firmware is not compatible with Arduino Uno as it is running at 115,200 baud
Uno requires 9600 baud. 
Possible to change firmware on sonar to be compatible with Uno and 9600 baud by using Blue Robotics "Ping viewer" application
^Tried this using serial to tty connecter and was unsuccessful, so it was decided to stick with Arduino Mega

Software mismatch may happen when trying to run sonarROS with ROS, the way this particular issue was solved was by opening the helloworld code
from the ROS beginner_tutorials and copy pasting the code.

For talker listener on ROS -> run:
Terminal 1: roscore
Terminal 2: cd catkin_ws
            source .devel/setup.bash
            rosrun beginner_tutorials talker.py
Terminal 3: cd catkin_ws
            source .devel/setup.bash
            rosrun beginner_tutorials listener.py
            
            
to run Arduino and ROS together, upload sonarROS to arduino

Terminal 1: roscore
Terminal 2: rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600

to see which ever output you want i.e. distance in inches, mm, or confidence

in new terminal type:
rostopic echo chatter -> distance in mm
rostopic echo chatte -> distance in inches
rostopic echo chatt -> confidence
