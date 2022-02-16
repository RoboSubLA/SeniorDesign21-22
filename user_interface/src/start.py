#!/usr/bin/env python
import Tkinter as tk
from controller import UserInterface


root = tk.Tk()
root.title('Robosub')
#root.geometry('1800x1200')

import rospy
from std_msgs.msg import String


UserInterface(root).pack(side="top", fill="both", expand=True)
root.mainloop()