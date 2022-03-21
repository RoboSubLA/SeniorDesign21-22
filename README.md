# Robosub
This document will hold all the information regarding our robosub.

## Design
We will use ROS to set up different nodes in our system. Some of the nodes will act as publishers and publish information known as topics. Each node has the opportunity to subscribe to different topics listening to the information that will be published. In this way the nodes can communicate among each other.

### System Overview
![Software Design Picture](https://github.com/RoboSubCSULA/SeniorDesign21-22/blob/main/software_design.jpg )

## Packages
These are a list of the different packages we have in this repository. 

### [user_interface](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/user_interface)
The user interface subscribe to all the different topics and display the data. 

### [mission_planning](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/mission_planning)
This node will be in charge of the state of the Robosub and decide what tasks it should do.


### [computer_vision](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/computer_vision)
This node will do image processing and image recognition to find targets. We will also implement machine learning for the image recognition.

### [sensing_and_actuation](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/sensing_and_actuation)
This node is where all our sensor and controls will be connected.

### [navigation](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/navigation)
This node will do path planning and mapping.

### [robosub_messages](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/robosub_messages)
We use this package to create all our messages that the robosub relies on. We have them all in the same package to make it easy to import into the other files. 

### [camera](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/camera)
...

### [robosub_launcher](https://github.com/RoboSubCSULA/SeniorDesign21-22/tree/main/robosub_launcher)
This package will be in charge of launching our system

## Getting Started
### Requirements:
- Python 2.7
- ROS Melodic
- Git
- Ubuntu 18.04 ( Not necessary for working with the code )

### To Start Working With The Code:

1. Clone this repo to your local machine
2. Branch out from the `main` branch and start working on your code.
4. When you're done working with your code submit PR and have someone review it.
5. If it is approved we will merge it with the `main` branch.

### Setting Up The Workspace:
This needs to be done in Ubuntu 18.04 with ROS Melodic installed.

1. Create a catkin workspace. Run the following commands in your terminal:
 - `mkdir -p ~/catkin_ws/src`
 - `cd ~/catkin_ws`
 - `catkin_make`

2. Next you want to clone this github repository to the `catkin_ws` folder.

3. Rename the repository folder `src`. You can run this command in the `catkin_ws` folder:  `mv <Repository Name> src`

4. Run `catkin_make` again.

4. Then in your `catkin_ws` folder run `source devel/setup.bash`. You will have to repeat this last step every time you open a new terminal.

### Starting The Robosub
We have the `robosub_launcher` package to help us launch the system. 

You can run these script to launch the system: 

`roslaunch robosub_launcher robosub.launch` to launch all the nodes.

`roslaunch robosub_launcher robosub_dummy.launch` this will launch the system in dummy mode where the sensors will publish dummy data to the system. 

### Useful Links:

[Competition Rules](https://robonation.org/app/uploads/sites/4/2021/04/RoboSub-2021-Mission-and-Rules__V1.pdf)

[How to work with git and github](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

[Installing ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu)

[Creating publisher & subscriber nodes with Python](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)



## Hardware

### Arduino Mega

### Nvidia Jetson TX2
