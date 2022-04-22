import Tkinter as tk
from robosub_messages.msg import IMU

class IMUWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.roll = None
        self.pitch = None
        self.yaw = None
        self.switch = True
        self.title = tk.Label(master=self, text='IMU', font=('arial', 14), width=10, pady=5,  bg='#8dc1c9')
        self.title.grid(row=0, column=0, columnspan=3, sticky='NEWS')

        self.roll_label_header = tk.Label(master=self, text='Roll', width=10, pady=10, font=('arial', 12))
        self.roll_label = tk.Label(master=self, text=self.roll, width=10, pady=5)
	self.roll_text = tk.Text(master = self, height = 1, width = 10)

        self.pitch_label_header = tk.Label(master=self, text='Pitch', width=10, pady=10, font=('arial', 12))
        self.pitch_label = tk.Label(master=self, text=self.pitch, width=10, pady=5)
	self.pitch_text = tk.Text(master = self, height = 1, width = 10)

        self.yaw_label_header = tk.Label(master=self, text='Yaw', width=10, pady=10, font=('arial', 12))
        self.yaw_label = tk.Label(master=self, text=self.yaw, width=10, pady=5)
	self.yaw_text = tk.Text(master = self, height = 1, width = 10)

	self.value_button = tk.Button(master = self, text = 'Enter', height = 1, command = self.sendData)


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
	self.roll_text.grid(row=3, column=0, sticky='news')

        self.pitch_label_header.grid(row=1, column=1, sticky='NEWS')
        self.pitch_label.grid(row=2, column=1, sticky='NEWS')
	self.pitch_text.grid(row=3, column=1, sticky='news')

        self.yaw_label_header.grid(row=1, column=2, sticky='NEWS')
        self.yaw_label.grid(row=2, column=2, sticky='NEWS')
	self.yaw_text.grid(row=3, column=2, sticky='news')

	self.value_button.grid(row = 4, column = 1, sticky = 'news')

    def sendData(self):
	# end-1c gets rid of the new line that from the input on text box
	roll_data = self.roll_text.get('1.0', 'end-1c')
	yaw_data = self.yaw_text.get('1.0', 'end-1c')
	pitch_data = self.pitch_text.get('1.0', 'end-1c')

	imu_msg = IMU()

	# replace('.', '', 1) is used along with isdecimal() to include decimal numbers for messages with float fields
	# otherwise just isdecimal() is used to check if the string is just an integer
	if roll_data and roll_data.isnumeric():
		imu_msg.roll = float(roll_data)
	else:
		imu_msg.roll = self.roll

	if yaw_data and yaw_data.isnumeric():
		imu_msg.yaw = float(yaw_data)
	else:
		imu_msg.yaw = self.yaw

	if pitch_data and pitch_data.isnumeric():
		imu_msg.pitch = float(pitch_data)
	else:
		imu_msg.pitch = self.pitch

	self.parent.imu_publisher.publish(imu_msg)

	# deletes the text from textbox after publishing message
	self.roll_text.delete('1.0', tk.END)
	self.yaw_text.delete('1.0', tk.END)
	self.pitch_text.delete('1.0', tk.END)
