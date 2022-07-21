import tkinter as tk

from settings import Settings
from src.guitar.fretboard import Fretboard
from src.guitar.string import String


class TuningFrame(tk.Frame):
    def __init__(self, settings: Settings):
        tk.Frame.__init__(self)
        self.settings = settings
        # TODO: implement
