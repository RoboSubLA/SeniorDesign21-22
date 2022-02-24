import Tkinter as tk

class DVLWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.roll = None
        self.pitch = None
        self.yaw = None
        self.switch = True
        self.title = tk.Label(master=self, text='DVL', width=10, pady=5,  bg='#88b1b8')
        self.title.grid(row=0, column=0, columnspan=3, sticky='NEWS')

        self.roll_label_header = tk.Label(master=self, text='Roll', width=10, pady=10, font=('arial', 8))
        self.roll_label = tk.Label(master=self, text=self.roll, width=10, pady=5)

        self.pitch_label_header = tk.Label(master=self, text='Pitch', width=10, pady=10, font=('arial', 8))
        self.pitch_label = tk.Label(master=self, text=self.pitch, width=10, pady=5)

        self.yaw_label_header = tk.Label(master=self, text='Yaw', width=10, pady=10, font=('arial', 8))
        self.yaw_label = tk.Label(master=self, text=self.yaw, width=10, pady=5)

        self.update_grid()


    def update(self, new_data):
        self.roll = new_data.roll
        self.pitch = new_data.pitch
        self.yaw = new_data.yaw

        text_roll = str(round(self.roll, 2))
        text_pitch = str(round(self.pitch, 2))
        text_yaw = str(round(self.yaw, 2))

        self.roll_label.config(text = text_roll)
        self.pitch_label.config(text = text_pitch)
        self.yaw_label.config(text = text_yaw)

        self.update_grid()

    def update_grid(self):
        self.roll_label_header.grid(row=1, column=0, sticky='NEWS')
        self.roll_label.grid(row=2, column=0, sticky='NEWS')
        self.pitch_label_header.grid(row=1, column=1, sticky='NEWS')
        self.pitch_label.grid(row=2, column=1, sticky='NEWS')
        self.yaw_label_header.grid(row=1, column=2, sticky='NEWS')
        self.yaw_label.grid(row=2, column=2, sticky='NEWS')