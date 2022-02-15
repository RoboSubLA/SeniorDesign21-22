#! /usr/bin/env python
import rospy


from dvl_driver import DVL
import matplotlib.pyplot as plt
from matplotlib import style


def main():
    style.use('fivethirtyeight')
    
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    # Change argument inside DVL according to what port the arduino is
    dvl = DVL("/dev/ttyACM0")
    dvl.start()



    while True:
        if dvl.has_data():
            data = dvl.get_data()
            print(str(data))


if __name__ == '__main__':
        main()
