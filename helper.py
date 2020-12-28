import tkinter as tk


class BLabel(object):
    b = ">>>"

    def __init__(self, master):

        self.l = tk.Label(master, bg="white")

    def add_option(self, text):
        if self.l.cget("text") == "":
            self.l.config(text=self.b + " " + text)
        else:
            self.l.config(text=self.l.cget("text") + "\n" + self.b + " " + text, font=("helvetica", 12))
