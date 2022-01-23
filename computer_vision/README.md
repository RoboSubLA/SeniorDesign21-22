# Computer Vision:
This node will do image processing and image recognition to find targets. We will also implement machine learning for the image recognition.

## How it works
... Explain short yolov4 and eventually other libraries that are being used. Link to documentation.

## How to work with the code
... How can a new developer start working with the code

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
