mega-sonar.ino - This code only works with Arduino Mega


sonarROS.ino - ran on Ubuntu 20.04, and ROS noetic 

Ping sonar firmware is not compatible with Arduino Uno as it is running at 115,200 baud
Uno requires 9600 baud. 
Possible to change firmware on sonar to be compatible with Uno and 9600 baud by using Blue Robotics "Ping viewer" application
^Tried this using serial to tty connecter and was unsuccessful, so it was decided to stick with Arduino Mega
