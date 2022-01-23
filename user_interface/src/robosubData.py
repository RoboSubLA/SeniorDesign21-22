import Tkinter as tk

class UserInterface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.header = Header(self, 'Sensors', '#a9d9db')
        self.header.pack(fill="both")
        self.view = AnalyticsView(self)
        self.view.pack(fill="both", expand=True)
        self.header2 = Header(self, 'Controls', '#a9d9db')
        self.header2.pack(fill="both")
