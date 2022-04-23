import Tkinter as tk
import rospy

from robosub_messages.msg import Hydrophones

class HydrophonesWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.direction = None
        self.switch = True
        self.title = tk.Label(master=self, text='Hydrophones', width=20, pady=5, font=('arial', 14),  bg='#88b1b8')
        self.title.pack(fill='both')
        self.info_label = tk.Label(master=self, text='Direction', width=20, pady=10, font=('arial', 12))
        self.info = tk.Label(master=self, text=self.direction, width=20, pady=5)
	self.direction_text = tk.Text(master = self, height = 1, width = 10)
	self.direction_button = tk.Button(master = self, text = 'Enter', height = 1, width = 4, command = self.sendData)

        self.info_label.pack()
        self.info.pack()
	self.direction_text.pack()
	self.direction_button.pack()


    def update(self, new_data):
        self.direction = new_data.direction
        self.info.config(text = str(round(self.direction, 2)))
        self.info.pack()

    def sendData(self):
	# end-1c gets rid of the new line that from the input on text box
	text_num = self.direction_text.get('1.0', 'end-1c')

	# replace('.', '', 1) is used along with isdecimal() to include decimal numbers for messages with float fields
	# otherwise just isdecimal() is used to check if the string is just an integer
	if text_num and text_num.isnumeric():
		hydro_msg = Hydrophones()
		hydro_msg.direction = float(text_num)
		self.parent.hydrophones_publisher.publish(hydro_msg)

	# deletes the text from textbox after publishing message
	self.direction_text.delete('1.0', tk.END)
