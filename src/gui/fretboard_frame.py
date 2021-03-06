import tkinter as tk

from src.gui.fret_widget import FretWidget
from src.guitar.fretboard import Fretboard
from src.notes.note import Note

# will be removed later
DEFAULT_FRETBOARD = Fretboard(24, [Note('E', 4), Note('B', 3), Note('G', 3), Note('D', 3), Note('A', 2), Note('E', 2)])


class FretboardFrame(tk.Frame):
    def __init__(self, init_fretbrd: Fretboard = DEFAULT_FRETBOARD, *args, **kwargs) -> None:
        tk.Frame.__init__(self, *args, **kwargs)
        self.fretbrd: Fretboard = init_fretbrd
        self.fret_dict: dict[tuple[int, int], FretWidget] = dict()

        self.configure_grid()
        self.create_widgets()

    def configure_grid(self) -> None:
        rows = list(range(self.fretbrd.get_str_num()))
        cols = list(range(max([a_string.get_frets() + 1 for a_string in self.fretbrd.get_strings()])))
        self.rowconfigure(rows, minsize=25, weight=1)
        self.columnconfigure(cols, minsize=50, weight=1)

    def create_widgets(self) -> None:
        for str_num, a_string in enumerate(self.fretbrd.get_strings()):
            for fret_num in a_string.get_range():
                pos_tuple = (str_num, fret_num)
                note = a_string.get_note_at_fret(fret_num)
                self.fret_dict[pos_tuple] = FretWidget(master=self, bound_note=note)
                self.fret_dict[pos_tuple].grid(row=str_num, column=fret_num, sticky='nsew')
