# Robosub
This document will hold all the information regarding our robosub.

## Getting Started
### Requirements:
- Python 2.7
- ROS Melodic
- Git
- Ubuntu 18.04 ( Not necessary for working with the code )

### To Start Working With The Code:

1. Clone this repo to your local machine
2. Fork the `dev` branch and name the new branch the feature you are working on.
3. When you're done working with your code submit PR and have someone review it.
4. If it is approved we will merge it with the `dev` branch.

### To Run The Code:
This needs to be done in Ubuntu 18.04 with ROS Melodic installed.

1. Create a catkin workspace. Run the following commands in your terminal:
 - `mkdir -p ~/catkin_ws/src`
 - `cd ~/catkin_ws`
 - `catkin_make`

2. Next you want to clone this github repository to the `catkin_ws` folder.

3. Rename the repository folder `src`. You can run this command in the `catkin_ws` folder:  `mv <Repository Name> src`

4. Run `catkin_make` again.


### Useful Links:

[How to work with git and github](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

[Installing ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu)

[Creating publisher & subscriber nodes with Python](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)


## Nodes
We will use ROS to set up different nodes in our system. A node works as a component which can subscribe to data from other nodes as well as publish their own data. This way we can break down our system, and work on the separate parts.

### [User Interface](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/UpdatingStructure/user_interface)
In the user interface we want to display sensor data, and logs.

### [Mission Planning](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/UpdatingStructure/mission_planning)
This node will be in charge of the state of the robosub and decide what tasks it should do.


### [Computer Vision](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/UpdatingStructure/computer_vision)
This node will do image processing and image recognition to find targets. We will also implement machine learning for the image recognition.

### [Sensing and Actuation](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/UpdatingStructure/sensing_and_actuation)
This node is where all our sensor and controls will be connected.

### [Guidance Navigation Control](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/UpdatingStructure/guidance_navigation_control)
This node will do path planning and mapping.


## Hardware

### Arduino Mega

### Nvidia Jetson TX2
