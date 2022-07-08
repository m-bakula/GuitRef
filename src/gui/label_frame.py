import tkinter as tk


class LabelFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def make_visible(self, text: str):
        pass

    def make_invisible(self):
        pass
