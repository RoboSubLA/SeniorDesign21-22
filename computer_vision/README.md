# Computer Vision:

This node will do image processing and image recognition to find targets. We will also implement machine learning for the image recognition.

Data:

`Object, label for the object found, string if no object is detected, will return'Null'`

`Confidence, float, 0 - 1, 1 being absolutely certainty. If no object is detected, returns -999`

`Vertical, int vertical distance in pixels of center of object to center of frame. 
Negative number means center of object is above center of image, positive means below.
returns = 999 if no object found`

`Horizontal, int horizontal distance in pixels of center of object to center of frame. 
Negative number means center of object is left of center of image, positive means right.
returns = 999 if no object found`
