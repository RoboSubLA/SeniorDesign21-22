import Tkinter as tk

class BarometerWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.depth = None
        self.confidence = None
        self.switch = True
        self.title = tk.Label(master=self, text='Barometer', width=10, pady=5,  bg='#d8e7e8')
        self.title.pack(fill='both')
        self.info = tk.Label(master=self, text=self.depth, width=10, pady=25)

        self.info.pack()


    def update(self, new_data):
        self.data = new_data
        self.depth = new_data.depth
        self.confidence = new_data.confidence

        new_text = str(round(self.depth, 2))

        self.info.config(text = new_text)
        self.info.pack()