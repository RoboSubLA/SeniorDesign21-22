import Tkinter as tk

class BarometerWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.depth = None
        self.confidence = None
        self.switch = True
        self.title = tk.Label(master=self, text='Barometer', width=10, pady=5,  bg='#88b1b8')
        self.title.grid(row=0, column=0, columnspan=2, sticky='NEWS')

        self.depth_label_header = tk.Label(master=self, text='Depth', width=10, pady=10, font=('arial', 8))
        self.depth_label = tk.Label(master=self, text=self.depth, width=10, pady=5)
        
        self.confidence_label_header = tk.Label(master=self, text='Confidence', width=10, pady=10, font=('arial', 8))
        self.confidence_label = tk.Label(master=self, text=self.confidence, width=10, pady=5)

        self.update_grid()


    def update(self, new_data):
        self.data = new_data
        self.depth = new_data.depth
        self.confidence = new_data.confidence

        text_depth = str(round(self.depth, 2))
        text_confidence = str(round(self.confidence, 2))

        self.depth_label.config(text = text_depth)
        self.confidence_label.config(text = text_confidence)
        self.update_grid()

    def update_grid(self):
        self.depth_label_header.grid(row=1, column=0, sticky='NEWS')
        self.depth_label.grid(row=2, column=0, sticky='NEWS')
        self.confidence_label_header.grid(row=1, column=1, sticky='NEWS')
        self.confidence_label.grid(row=2, column=1, sticky='NEWS')