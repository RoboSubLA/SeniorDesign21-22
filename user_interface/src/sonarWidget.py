import Tkinter as tk

class SonarWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.distance = None
        self.confidence = None
        self.switch = True
        self.title = tk.Label(master=self, text='Sonar', width=10, pady=5,  bg='#8dc1c9')
        self.title.grid(row=0, column=0, columnspan=2, sticky='NEWS')

        self.distance_label_header = tk.Label(master=self, text='Distance', width=10, pady=10, font=('arial', 8))
        self.distance_label = tk.Label(master=self, text=self.distance, width=10, pady=5)
        
        self.confidence_label_header = tk.Label(master=self, text='Confidence', width=10, pady=10, font=('arial', 8))
        self.confidence_label = tk.Label(master=self, text=self.confidence, width=10, pady=5)

        self.update_grid()


    def update(self, new_data):
        self.distance = new_data.distance
        self.confidence = new_data.confidence

        text_distance = str(round(self.distance, 2))
        text_confidence = str(round(self.confidence, 2))

        self.distance_label.config(text = text_distance)
        self.confidence_label.config(text = text_confidence)
        self.update_grid()

    def update_grid(self):
        self.distance_label_header.grid(row=1, column=0, sticky='NEWS')
        self.distance_label.grid(row=2, column=0, sticky='NEWS')
        self.confidence_label_header.grid(row=1, column=1, sticky='NEWS')
        self.confidence_label.grid(row=2, column=1, sticky='NEWS')