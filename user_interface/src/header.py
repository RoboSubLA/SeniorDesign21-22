import Tkinter as tk

class Header(tk.Frame):
    def __init__(self, parent, text, color, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        fontStyle = tkFont.Font(family="Lucida Grande", size=15)
        lbl_logo = tk.Label(master=self, text=text, bg=color, padx=15, font = fontStyle)
        lbl_logo.pack(fill="both", expand=True)
