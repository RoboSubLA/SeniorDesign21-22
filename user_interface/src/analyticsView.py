import Tkinter as tk
from analyticsWidget import AnalyticsWidget

class AnalyticsView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.barometerDisplay = AnalyticsWidget(self,'Depth', '2m', 20)
        self.sonarDisplay = AnalyticsWidget(self,'Distance To Obj', '7m', 20)
        self.hydrophonesDisplay = AnalyticsWidget(self,'Ping Degrees', '75', 20)
        self.imuDisplay = AnalyticsWidget(self,'IMU', '2m', 30)
        self.dviDisplay = AnalyticsWidget(self,'DVI', 'XYZ', 30)


        self.barometerDisplay.grid(row=0, column=0, columnspan=4)
        self.sonarDisplay.grid(row=0, column=4, columnspan=4)
        self.hydrophonesDisplay.grid(row=0, column=8, columnspan=4)
        self.imuDisplay.grid(row=1, column=0, columnspan=6)
        self.dviDisplay.grid(row=1, column=6, columnspan=6)
