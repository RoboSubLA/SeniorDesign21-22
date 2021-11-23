#! /usr/bin/env python
import tkinter as tk
import rospy

from user_interface import UserInterface

rospy.init_node('user_interface')

root = tk.Tk()
root.title('Robosub')
#root.geometry("1200x800")
UserInterface(root).pack(side="top", fill="both", expand=True)
root.mainloop()
