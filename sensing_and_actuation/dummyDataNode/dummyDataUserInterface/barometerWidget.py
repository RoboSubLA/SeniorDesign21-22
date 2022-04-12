import Tkinter as tk
from robosub_messages.msg import Barometer

class BarometerWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.depth = None
        self.temperature = None
        self.switch = True
        self.title = tk.Label(master=self, text='Barometer', font=('arial', 14), width=10, pady=5,  bg='#88b1b8')
        self.title.grid(row=0, column=0, columnspan=2, sticky='NEWS')

        self.depth_label_header = tk.Label(master=self, text='Depth', width=10, pady=10, font=('arial', 12))
        self.depth_label = tk.Label(master=self, text=self.depth, width=10, pady=5)
	self.depth_text = tk.Text(master=self, width = 10, height = 1)
        
        self.temperature_label_header = tk.Label(master=self, text='Temperature', width=10, pady=10, font=('arial', 12))
        self.temperature_label = tk.Label(master=self, text=self.temperature, width=10, pady=5)
	self.temperature_text = tk.Text(master=self, width = 10, height = 1)

	self.value_button = tk.Button(master = self, text = 'Enter', height = 1, command = self.sendData)

        self.update_grid()


    def update(self, new_data):
        self.data = new_data
        self.depth = new_data.depth
        self.temperature = new_data.temperature

        text_depth = str(round(self.depth, 2))
        text_temperature = str(round(self.temperature, 2))

        self.depth_label.config(text = text_depth)
        self.temperature_label.config(text = text_temperature)
        self.update_grid()

    def update_grid(self):
        self.depth_label_header.grid(row=1, column=0, sticky='NEWS')
        self.depth_label.grid(row=2, column=0, sticky='NEWS')
	self.depth_text.grid(row = 3, column = 0, sticky='NEWS')

        self.temperature_label_header.grid(row=1, column=1, sticky='NEWS')
        self.temperature_label.grid(row=2, column=1, sticky='NEWS')
	self.temperature_text.grid(row = 3, column = 1, sticky = 'NEWS')

	self.value_button.grid(row = 4, column = 1, sticky='NEWS')

    def sendData(self):
	# end-1c gets rid of the new line that from the input on text box
	depth_data = self.depth_text.get('1.0', 'end-1c')
	temperature_data = self.temperature_text.get('1.0', 'end-1c')

	barometer_msg = Barometer()

	# replace('.', '', 1) is used to also include decimal numbers for messages with float fields
	if depth_data and depth_data.replace('.', '', 1).isdecimal():
		barometer_msg.depth = float(depth_data)
	else:
		barometer_msg.depth = self.depth

	if temperature_data and temperature_data.replace('.', '', 1).isdecimal():
		barometer_msg.temperature = float(temperature_data)
	else:
		barometer_msg.temperature = self.temperature

	self.parent.barometer_publisher.publish(barometer_msg)

	# deletes the text from textbox after publishing message
	self.depth_text.delete('1.0', tk.END)
	self.temperature_text.delete('1.0', tk.END)
