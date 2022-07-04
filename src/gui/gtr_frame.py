import tkinter as tk

from src.guitar.fretboard import Fretboard
from src.notes.note import Note

# will be removed later
DEFAULT = Fretboard(24, [Note('E', 4), Note('B', 3), Note('G', 3), Note('D', 3), Note('A', 2), Note('E', 2)])


class GtrFrame(tk.Frame):
    def __init__(self, init_fretbrd: Fretboard = DEFAULT, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.fretbrd: Fretboard = init_fretbrd

        self.configure_grid()
        self.update_labels()

    def update_labels(self):
        pass

    def configure_grid(self):
        pass
