import Tkinter as tk
from robosub_messages.msg import Sonar

class SonarWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.distance = None
        self.confidence = None
        self.switch = True
        self.title = tk.Label(master=self, text='Sonar', font=('arial', 14), width=10, pady=5,  bg='#8dc1c9')
        self.title.grid(row=0, column=0, columnspan=2, sticky='NEWS')

        self.distance_label_header = tk.Label(master=self, text='Distance', font=('arial', 12), width=10, pady=10)
        self.distance_label = tk.Label(master=self, text=self.distance, width=10, pady=5)
	self.distance_text = tk.Text(master=self, height = 1, width = 10)
        
        self.confidence_label_header = tk.Label(master=self, text='Confidence', font=('arial', 12), width=10, pady=10)
        self.confidence_label = tk.Label(master=self, text=self.confidence, width=10, pady=5)
	self.confidence_text = tk.Text(master=self, height = 1, width = 10)

	self.value_button = tk.Button(master = self, text = 'Enter', height = 1, command = self.sendData)

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
	self.distance_text.grid(row = 3, column = 0, sticky = 'news')

        self.confidence_label_header.grid(row=1, column=1, sticky='NEWS')
        self.confidence_label.grid(row=2, column=1, sticky='NEWS')
	self.confidence_text.grid(row = 3, column = 1, sticky = 'news')

	self.value_button.grid(row = 4, column = 1)

    def sendData(self):
	# end-1c gets rid of the new line that from the input on text box
	distance_data = self.distance_text.get('1.0', 'end-1c')
	confidence_data = self.confidence_text.get('1.0', 'end-1c')

	sonar_msg = Sonar()

	# replace('.', '', 1) is used along with isdecimal() to include decimal numbers for messages with float fields
	# otherwise just isdecimal() is used to check if the string is just an integer
	if distance_data and distance_data.replace('.', '', 1).isdigit():
		sonar_msg.distance = float(distance_data)
	else:
		sonar_msg.distance = self.distance

	if confidence_data and confidence_data.replace('.', '', 1).isdigit():
		sonar_msg.confidence = float(confidence_data)
	else:
		sonar_msg.confidence = self.confidence

	self.parent.sonar_publisher.publish(sonar_msg)

	# deletes the text from textbox after publishing message
	self.distance_text.delete('1.0', tk.END)
	self.confidence_text.delete('1.0', tk.END)

