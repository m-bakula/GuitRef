import tkinter as tk

from settings import Settings


class LabelFrame(tk.Frame):
    def __init__(self, settings: Settings, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.settings = settings

    def make_visible(self, text: str):
        pass

    def make_invisible(self):
        pass
