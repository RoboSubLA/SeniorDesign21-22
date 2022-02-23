import Tkinter as tk

class SonarWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.distance = None
        self.confidence = None
        self.switch = True
        self.title = tk.Label(master=self, text='Sonar', width=10, pady=5,  bg='#d8e7e8')
        self.title.pack(fill='both')
        self.info = tk.Label(master=self, text=self.distance, width=10, pady=25)

        self.info.pack()


    def update(self, new_data):
        self.distance = new_data.distance
        self.confidence = new_data.confidence

        new_text = str(round(self.distance))

        self.info.config(text = new_text)
        self.info.pack()