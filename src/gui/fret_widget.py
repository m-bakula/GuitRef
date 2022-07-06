import tkinter as tk

from src.notes.note import Note


class FretWidget(tk.Label):
    def __init__(self, bound_note: Note, *args, **kwargs) -> None:
        tk.Label.__init__(self, text=bound_note.get_name(), relief='ridge', *args, **kwargs)
        self.note: Note = bound_note
        self.highlight: bool = False
        self.highlight_col: str = 'red'

    def highlight_on(self) -> None:
        self.highlight = True

    def highlight_off(self) -> None:
        self.highlight = False

    def change_color(self, color_str: str) -> None:
        self.highlight_col = color_str
