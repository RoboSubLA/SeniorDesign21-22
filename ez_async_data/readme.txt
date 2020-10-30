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

