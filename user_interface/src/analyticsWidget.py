import Tkinter as tk

class AnalyticsWidget(tk.Frame):
    def __init__(self, parent, title, data, width, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.data = data
        self.switch = True
        self.title = tk.Label(master=self, text=title, width=width, pady=5,  bg='#d8e7e8')
        self.title.pack(fill='both')

        self.info = tk.Label(master=self, text=data, width=width, pady=25)


        self.info.pack()


    def update(self, new_data):
        self.data = new_data
        self.info.config(text = self.data)
