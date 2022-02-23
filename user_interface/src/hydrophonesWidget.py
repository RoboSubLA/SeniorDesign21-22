import Tkinter as tk

class HydrophonesWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.direction = None
        self.switch = True
        self.title = tk.Label(master=self, text='IMU', width=10, pady=5,  bg='#d8e7e8')
        self.title.pack(fill='both')
        self.info = tk.Label(master=self, text=self.direction, width=10, pady=25)


        self.info.pack()


    def update(self, new_data):
        self.direction = new_data.direction
        self.info.config(text = str(round(self.direction, 2)))
        self.info.pack()