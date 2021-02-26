# ROBOSUB SOFTWARE README

## This software is intended to be installed as the src folder in a catking workspace

# make the catking workspace
mkdir -p ~/catkin_ws/src
cd ~/catkin
catkin_make

# Download the repository
While in the catkin directory
git clone [ssh-repo_link located in gitub]

# rename the downloaded folder to src
mv [foldername] src

# make the catkin dierctory again
catkin_make

### There should be a longer make time, accessing files inside each package
## if all goes well no errors should occur
## please refer to each packages readme to understand its function



# TODO
## Data Logging
when making the launch script make sure to add the following line
find out how to make it point to a directory to make the file
default is the directory the command is run
command will record all output on every topic
$rosbag record -a

top play back a data file for testing purposes
$rosbag play [filename]


## backups
rsync - used for data backup

