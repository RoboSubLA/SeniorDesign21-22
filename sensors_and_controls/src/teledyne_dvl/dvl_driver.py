import serial
import time
from threading import Thread, Lock

class Msg:
    def __init__(self):
        self.xvel = 0
        self.yvel = 0
        self.zvel = 0
        self.xpos = 0
        self.ypos = 0
        self.zpos = 0
        self.yaw = 0
        self.pitch = 0
        self.roll = 0
        self.depth = 0

        self.timestamp = 0

    def __str__(self):
	# Temporary return statement
	# Syntax error with other return statement
	return 'xvel={0}\nyvel={1}\nzvel={2}\n' \
		'xpos={3}\nypos={4}\nzpos={5}\n' \
		'yaw={6}\npitch={7}\nroll={8}'.format(self.xvel, self.yvel, self.zvel, self.xpos, self.ypos, self.zpos, self.yaw, self.pitch, self.roll)
	
	# Below return statement has f-string which was introduced in python 3.6
        # return f'xvel={self.xvel}\tyvel={self.yvel}\tzvel={self.zvel}\n' \
        #       f'xpos={self.xpos}\typos={self.ypos}\tzpos={self.zpos}\n' \
        #       f'pitch={self.pitch}\tyaw{self.yaw}\troll={self.roll}\n'

class DVL(Thread):


    def __init__(self, port):
        Thread.__init__(self)
        self.serial = serial.Serial(port=port, baudrate=115200)
	print('Port: {0}'.format(port))
        #for threading data purposes
        self.mutex = Lock()

        self.msg = Msg()
        self.data_flag = False

    # Original write function
    # Might be causing problems because the syntax was introduced in a later version of python
    # def write(self, output: str) -> None:
    #     self.serial.write(output.encode())

    # New write function because syntax errors from the original function was causing problems
    # Might not produce the same functionality as the previous version
    def write(self, output):
        self.serial.write(output.encode())

    def has_data(self):
        self.mutex.acquire()
        flag = self.data_flag
        self.mutex.release()
        return flag

    def get_data(self):
        self.mutex.acquire()
        data = self.msg
        self.data_flag = False
        self.mutex.release()
        return data

    def run(self):
        #start the communication needs to send the break
        self.serial.write(b"===")  # DVL Break (PathFinder Guide p. 24 and p.99)

        time.sleep(2)
        # rospy.sleep(5)  # sleep for 2 seconds

        # ROS publisher setup
        # pub = rospy.Publisher('dvl_status', DVL, queue_size=1)
        # # pubHeading = rospy.Publisher('dvl_heading', Float32, queue_size = 1)
        # pubSS = rospy.Publisher('dvl_ss', Float32, queue_size=1)
        # rospy.Subscriber('current_rotation', Rotation, self.rCallBack, queue_size=1)
        # msg = DVL()
        # # msgHeading = Float32()
        # msgSS = Float32()

        # PD6 settings --------------------------------------------------------------
        self.write("CR1\r")  # set factory defaults.(Pathfinder guide p.67)
        self.write("CP1\r")  # required command
        # PD6 settings --------------------------------------------------------------
        self.write("PD6\r")  # pd6 data format (Pathfinder Guide p.207) <---important
        # dvl.write("BK0\r")
        # PD13 settings -------------------------------------------------------------
        # dvl.write("PD13\r")
        self.write("EX11110\r")  # coordinate transformation (Pathfinder guide p.124)
        self.write("EA+4500\r")  # heading alignment (Pathfinder guide 118)
        # dvl.write("EZ11110010\r") #internal speed of sound, depth, heading, pitch, roll, temperature
        self.write("EZ11000010\r")  # internal speed of sound, depth, temperature
        # dvl.write("EZ10000010\r") #default sensor source (Pathfinder guide 125)
        # dvl.write("EZ11011010\r") #internal speed of sound, depth, pitch, roll, temperature
        # dvl.write("EZ10000010\r") #internal speed of sound, temperature

        self.write("CK\r")  # stores present parameters (Pathfinder guide 114)
        self.write("CS\r")  # start pinning (Pathfinder guide 115)

        # NOTE: the \r character is required for continuous stream i.e (PD6\r")

        print("dvl start")

        loop_time = time.time()
        pubTimePrev = loop_time
        # pubTimeInterval = 0.01
        heading_time_prev = loop_time
        heading_time_interval = 0.014
        mod_val = 0
        # while not rospy.is_shutdown():

        while True:
            loop_time = time.time()
            if self.serial.in_waiting > 0:  # If there is a message from the DVL
                try:
                    line = self.serial.readline()
                    # print(line)

                    line = str(line)
		    lineSplit = line.split(",")

                    # print(line)
		    # Code underneath sends to Msg class and prints
		    self.msg.xvel = lineSplit[0]
		    self.msg.yvel = lineSplit[1]
		    self.msg.zvel = lineSplit[2]

		    self.msg.xpos = lineSplit[3]
		    self.msg.ypos = lineSplit[4]
		    self.msg.zpos = lineSplit[5]

		    self.msg.yaw = lineSplit[6]
		    self.msg.pitch = lineSplit[7]
		    self.msg.roll = lineSplit[8]

		    print(self.msg.__str__())

                except:
                    print("read fail")
                #
                # print(line)

                if ":BD" in line:  # If the message is a positional update
                    line = line.split(",")
                    # north_trans = float(line[1])
                    # east_trans = float(line[2])
                    east_trans = float(line[1])
                    north_trans = float(line[2])
                    up_trans = float(line[3])
                    rangeToBottom = float(line[4])
                    # print(line[5].split('\\')[0])
                    timeDifference = float(line[5].split("\\")[0])
                    # setup msg to be published to ROS

                    self.mutex.acquire()
                    self.xpos = east_trans
                    self.ypos = north_trans
                    self.zpos = up_trans
                    self.data_flag = True
                    self.depth = rangeToBottom
                    self.mutex.release()

                    # pub.publish(msg)
                    # print(self.__str__())

                elif ":BS" in line:  # If the message is a velocity update
                    line = line.split(",")
                    port_vel = float(line[1])
                    aft_vel = float(line[2])
                    up_vel = float(line[3])
                    status = line[4]
                    self.mutex.acquire()
                    self.msg.xvel = port_vel  # need to change msg var names
                    self.msg.yvel = aft_vel
                    self.msg.zvel = up_vel
                    self.data_flag = True
                    self.mutex.release()

                    # print(str(self))
                    # pub.publish(msg)

                elif ":SA" in line:
                    line = line.split(",")
                    self.mutex.acquire()
                    self.pitch = line[1]
                    self.roll = line[3][:-5]
                    self.yaw = line[2]
                    self.data_flag = True
                    self.mutex.release()


                elif ":TS" in line:  # If the message is a timestamp
                    line = line.split(",")
                    # msgSS.data = float(line[5])
                    self.mutex.acquire()
                    self.timestamp = float(line[5])
                    self.data_flag = True
                    self.mutex.release()
                    # print(f'timestamp: {float(line[5])}')
                    # pubSS.publish(msgSS)
