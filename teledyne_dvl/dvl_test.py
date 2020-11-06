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
        return f'xvel={self.xvel}\tyvel={self.yvel}\tzvel={self.zvel}\n' \
               f'xpos={self.xpos}\typos={self.ypos}\tzpos={self.zpos}\n' \
               f'pitch={self.pitch}\tyaw{self.yaw}\troll={self.roll}\n'

class DVL:
    def __init__(self, port):
        Thread.__init__(self)
        self.serial = serial.Serial(port=port, baudrate=115200,
                                    bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        #for threading data purposes
        self.mutex = Lock()

        self.msg = Msg()
        self.data_flag = False

        # start the communication needs to send the break
        self.serial.write(b"===")  # DVL Break (PathFinder Guide p. 24 and p.99)
        #8
        self.get_response()
        time.sleep(2)
        #dvl ready to accept commands

    def self_tests(self):
        ###noise, elect, ceramic test
        self.write('pt5')
        #10
        response = self.get_response()
        for line in response:
            if b"FAILED" in line:
                return False

        ##general test
        # self.write('pa')
        # #15
        # response = self.get_response()
        # # if len(response) != 12:
        # #     print (response)
        # for line in response:
        #     if b"NOGO" in line or b"NO-GO" in line:
        #         return False

        return True

    def setup_dvl_options(self):
        # PD6 settings --------------------------------------------------------------
        self.write("CR1")  # set factory defaults.(Pathfinder guide p.67)
        self.write("CP1")  # required command
        # PD6 settings --------------------------------------------------------------
        self.write("PD6")  # pd6 data format (Pathfinder Guide p.207) <---important
        # dvl.write("BK0\r")
        # PD13 settings -------------------------------------------------------------
        # dvl.write("PD13\r")
        self.write("EX11110")  # coordinate transformation (Pathfinder guide p.124)
        self.write("EA+4500")  # heading alignment (Pathfinder guide 118)
        # dvl.write("EZ11110010\r") #internal speed of sound, depth, heading, pitch, roll, temperature
        self.write("EZ11000010")  # internal speed of sound, depth, temperature
        # dvl.write("EZ10000010\r") #default sensor source (Pathfinder guide 125)
        # dvl.write("EZ11011010\r") #internal speed of sound, depth, pitch, roll, temperature
        # dvl.write("EZ10000010\r") #internal speed of sound, temperature

        self.write("CK")  # stores present parameters (Pathfinder guide 114)
        self.write("CS")  # start pinning (Pathfinder guide 115)

        # NOTE: the \r character is required for continuous stream i.e (PD6\r")

    def write(self, output: str) -> None:
        output = output+'\r'
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

    # def get_response(self, expected):
    #     time.sleep(.5)
    #     response = []
    #     while len(response) < expected:
    #         while self.serial.in_waiting > 0:
    #             line = self.serial.readline()
    #             # for b in line:
    #             #     print (b)
    #             print(line)
    #             response.append(line)
    #     return response
    def get_response(self):
        time.sleep(.5)
        response = []
        line = b''
        while line != b'>':
            while self.serial.in_waiting > 0:
                line = self.serial.readline()
                # for b in line:
                #     print (b)
                print(line)
                response.append(line)
        return response

    def run(self):
        # rospy.sleep(5)  # sleep for 2 seconds

        # ROS publisher setup
        # pub = rospy.Publisher('dvl_status', DVL, queue_size=1)
        # # pubHeading = rospy.Publisher('dvl_heading', Float32, queue_size = 1)
        # pubSS = rospy.Publisher('dvl_ss', Float32, queue_size=1)
        # rospy.Subscriber('current_rotation', Rotation, self.rCallBack, queue_size=1)
        # msg = DVL()
        # # msgHeading = Float32()
        # msgSS = Float32()

        print("dvl start")

        # loop_time = time.time()
        # pubTimePrev = loop_time
        # pubTimeInterval = 0.01
        # heading_time_prev = loop_time
        # heading_time_interval = 0.014
        # mod_val = 0
        # while not rospy.is_shutdown():

        while True:
            # loop_time = time.time()

            if self.serial.in_waiting > 0:  # If there is a message from the DVL
                try:
                    line = self.serial.readline()
                    # print(line)
                    line = str(line)
                    # print(line)
                    # print(line)
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

                    # self.mutex.acquire()
                    # self.xpos = east_trans
                    # self.ypos = north_trans
                    # self.zpos = up_trans
                    # self.data_flag = True
                    # self.depth = rangeToBottom
                    # self.mutex.release()
                    print(f'xpos: {east_trans}, ypos: {north_trans}, zpos: {up_trans}')

                    # pub.publish(msg)
                    # print(self.__str__())

                elif ":BS" in line:  # If the message is a velocity update
                    line = line.split(",")
                    port_vel = float(line[1])
                    aft_vel = float(line[2])
                    up_vel = float(line[3])
                    status = line[4]
                    # self.mutex.acquire()
                    # self.msg.xvel = port_vel  # need to change msg var names
                    # self.msg.yvel = aft_vel
                    # self.msg.zvel = up_vel
                    # self.data_flag = True
                    # self.mutex.release()

                    print(f'xvel: {port_vel}, yvel: {aft_vel}, zvel: {up_vel}')

                    # print(str(self))
                    # pub.publish(msg)

                elif ":SA" in line:
                    line = line.split(",")
                    # self.mutex.acquire()
                    self.pitch = line[1]
                    self.roll = line[2]
                    self.yaw = line[3][:-2]
                    # self.data_flag = True
                    # self.mutex.release()
                    print(f'Pitch: {self.pitch}, Yaw: {self.yaw}, Roll: {self.roll}')


                elif ":TS" in line:  # If the message is a timestamp
                    line = line.split(",")
                    # msgSS.data = float(line[5])
                    # self.mutex.acquire()
                    self.timestamp = float(line[5])
                    self.data_flag = True
                    # self.mutex.release()
                    print(f'timestamp: {line[1][8:]}')
                    # pubSS.publish(msgSS)

if __name__ == '__main__':
    dvl = DVL('Com4')
    time.sleep(2)
    dvl.self_tests()
    time.sleep(2)
    print("setting DVL")
    dvl.setup_dvl_options()
    time.sleep(2)
    dvl.run()

