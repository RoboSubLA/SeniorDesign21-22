# Robosub
This document will hold all the information regarding our robosub.

## Getting Started
#### Requirements:
- Python 2.7
- ROS Melodic
- Git
- Ubuntu 18.04 ( Not necessary for working with the code )

#### To Start Working With The Code:

1. Clone this repo to your local machine
2. Fork the `dev` branch and name the new branch the feature you are working on.
3. When you're done working with your code submit PR and have someone review it.
4. If it is approved we will merge it with the `dev` branch.

#### To Run The Code:

1. Create a catkin workspace. Run the following commands in your terminal:
 - `mkdir -p ~/catkin_ws/src`
 - `cd ~/catkin_ws`
 - `catkin_make`

2. Next you want to clone this github repository to the `catkin_ws` folder.

3. ... (this is uncompleted)

Useful Links:

[How to work with git and github](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

[Installing ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu)


## Nodes
We will use ROS to set up different nodes in our system. A node works as a component which can subscribe to data from other nodes as well as publish their own data. This way we can break down our system, and work on the separate parts.

#### User Interface
The user interface is where we display
 - Video
 - Sensor Data
 - Logs
 - Parameter Calibration & Selection


#### Mission Planning
This node will be in charge of planning

`Publishes: Task & desired action	`

#### Target Recognition
This node will do image processing and image recognition to find targets. We will also implement machine learning for the image recognition.
`Publishes: Target`

#### Sensing and Actuation
This node is where all our sensor and controls will be connected.

Sensors:
-   DVL - xyz
-   Sonar - dist to obj (m)
-   Barometer - depth (m)
-   Hydrophones

Controls:
 - Thrusters
 - Cooling pump
 - Torpedo
 - Claw
 - Dropper

`Publishes: Sensor Information`
#### Guidance Navigation Control
This node will do path planning and mapping.

`Publishes: Control Command`

#### Cooling
This node will be in charge of cooling the Robosub. It will monitor the heat of the Robosub and act on that information.

`Publishes: Pump Command`

#### Camera
This node will interface with the camera and do image filtering.

`Publishes: Image/Video`
