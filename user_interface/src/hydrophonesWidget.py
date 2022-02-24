import Tkinter as tk


class HydrophonesWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.direction = None
        self.switch = True
        self.title = tk.Label(master=self, text='Hydrophones', width=20, pady=5,  bg='#88b1b8')
        self.title.pack(fill='both')
        self.info_label = tk.Label(master=self, text='Direction', width=20, pady=10, font=('arial', 8))
        self.info = tk.Label(master=self, text=self.direction, width=20, pady=5)

        self.info_label.pack()
        self.info.pack()


    def update(self, new_data):
        self.direction = new_data.direction
        self.info.config(text = str(round(self.direction, 2)))
        self.info.pack()