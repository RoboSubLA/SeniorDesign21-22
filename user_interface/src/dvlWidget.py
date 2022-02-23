import Tkinter as tk

class DVLWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.data = None
        self.switch = True
        self.title = tk.Label(master=self, text='DVL', width=10, pady=5,  bg='#d8e7e8')
        self.title.pack(fill='both')
        self.info = tk.Label(master=self, text=self.data, width=10, pady=25)


        self.info.pack()


    def update(self, new_data):
        self.data = new_data
        self.info.config(text = self.data.roll)
        self.info.pack()