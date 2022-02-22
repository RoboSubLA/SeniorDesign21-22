# Computer Vision:
This node is primarily based on image processing and image recognition to help dectect colored targets, objects, and borders. We will also implement machine learning for the image recognition.

## How it works
Yolo uses machine learning to identify objects in an image. Yolo can return an image with a label, confidence, and a box surrounding the object. We can use this information to detect the bin's background (White), cover (Orange), and handle (Purple) as well as the torpedo border (Red) and the octagon's background (Orange). We can also use this information to determine the position of the images to align the sub with the desired object.

![image](https://user-images.githubusercontent.com/61888693/155066634-d7d0121b-7155-466a-bfaf-e7f3ece98926.png)
![image](https://user-images.githubusercontent.com/61888693/155066686-ad0c03c1-b69b-4164-b4d5-d97817d3f3dc.png)
![image](https://user-images.githubusercontent.com/61888693/155066721-7269f4b7-7eeb-4eda-8292-5ea9f797253e.png)
![image](https://user-images.githubusercontent.com/61888693/155066821-48f6605e-77d4-4a62-b037-1ea26184dc38.png)

## How to work with the code
Use a computer with Ubuntu installed to use ROS.

Open the terminal

`git clone https://github.com/RoboSubCSULA/SeniorDesign21-22.git`

`cd computer_vision`

create a branch with `git checkout -b <branch name>`

You can now begin working on the code in your local environment

### Push your code

After you have made your changes push your code to be approved

`git add -A`

`git commit -m "brief description of the changes made"`

`git push origin`

On the github website, create a pull request and add team members to look over your code and add their approval if all is correct.

## Testing
... How can you test the different states

## Data it publishes

Data:

`Object, label for the object found, string if no object is detected, will return'Null'`

`Confidence, float, 0 - 1, 1 being absolutely certainty. If no object is detected, returns -999`

`Vertical, int vertical distance in pixels of center of object to center of frame.
Negative number means center of object is above center of image, positive means below.
returns = 999 if no object found`

`Horizontal, int horizontal distance in pixels of center of object to center of frame.
Negative number means center of object is left of center of image, positive means right.
returns = 999 if no object found`
