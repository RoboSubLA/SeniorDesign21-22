###########
#IMU information
#running as c++ program using Libraries from Vectornav
#libraries are included in this package
#data aquasition program source code located in /src/main.cpp
#Program outputs a custom message 
	#message name for import "Rotation"
	#composed of
		float32 roll
		float32 pitch
		float32 yaw
    #Topic name
        current_rotation

        
####IMU LOGS
#uses rosbag
    #data structure to store data being published
    
#stores all topics
#running rosbag record with the #option -a, indicating that all published topics should be #accumulated in a bag file.
rosbag record -a

#recording a subset of data
rosbag record -O [filename] [topic1] [topic2]

#commands will make a bagfile in the current directory

#Getting the IMU working
#find the tty connection the vectornav is connected to
#some trial and error expected
#make appropriate changed to the device name in the cpp file

#find usb dev
dmesg | grep tty

#change in /src/main.cpp if necessary
#default is '/dev/ttyUSB0'


#if permission errors occur

#add user to dialout to allou connections to USB devices
sudo usermod -a -G dialout $USER

#make sure to log out and log in toapply the change

#==============================================================#

#Using 2018 code
#todo need to find out what types the msg is being sent as
#find out how to use msg type from other packages

