# Computer Vision:
This node will do image processing and image recognition to find targets. We will also implement machine learning for the image recognition.

## How it works
... Explain short yolov4 and eventually other libraries that are being used. Link to documentation.

## How to work with the code
... How can a new developer start working with the code

Have all required packages installed from the RoboSubCSULA README.md\

Before running any of the commands when testing the LetterA 
I. Locate the LetterA.data file within the yolov4_files folder within the catkin_ws
II. For the "names" value within the LetterA.data file change the path to your local path for LetterA.names file within the yolov4_files folder.

1. run following commands in your system's terminal:
- `cd catkin_ws`
- `catkin_make`
- `source devel/setup.bash`
- `roscore`

2. Create a new terminal and run the following commands;
- `cd catkin_ws`
- `source devel/setup.bash`
- `rosrun computer_vision cv_start.py`

alternative to step 2:
- `cd src/computer_vision/`
- `python cv_start.py`



## Testing
... How can you test the different states

## Data it publishes
... What data will the ROS package publish.

Data:

`Object, label for the object found, string if no object is detected, will return'Null'`

`Confidence, float, 0 - 1, 1 being absolutely certainty. If no object is detected, returns -999`

`Vertical, int vertical distance in pixels of center of object to center of frame.
Negative number means center of object is above center of image, positive means below.
returns = 999 if no object found`

`Horizontal, int horizontal distance in pixels of center of object to center of frame.
Negative number means center of object is left of center of image, positive means right.
returns = 999 if no object found`
