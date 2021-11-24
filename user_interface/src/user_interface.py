#! /usr/bin/env python

import Tkinter as tk
from header import Header
from analyticsView import AnalyticsView


import rospy
from sensing_and_actuation.msg import sensing_and_actuation_data

class UserInterface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.robosub_data = None
        self.header = Header(self, 'Sensors', '#a9d9db')
        self.header.pack(fill="both")
        self.view = AnalyticsView(self, robosub_data)
        self.view.pack(fill="both", expand=True)
        self.header2 = Header(self, 'Controls', '#a9d9db')
        self.header2.pack(fill="both")

        self.clock()

    def update(self, data):
        self.robosub_data = data
        self.analyticsView.update()

    def clock(self):
        rospy.Subscriber('sensing_and_actuation_data', sensing_and_actuation_data, update)
        self.after(100, self.clock)
