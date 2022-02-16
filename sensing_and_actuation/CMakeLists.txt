cmake_minimum_required(VERSION 3.0.2)
project(sensing_and_actuation)


## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  sensing_and_actuation_data.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
)
###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  # include
  ${catkin_INCLUDE_DIRS}
)

