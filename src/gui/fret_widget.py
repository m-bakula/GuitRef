import tkinter as tk

from settings import Settings
from src.notes.note import Note


class FretWidget(tk.Label):
    def __init__(self, settings: Settings, bound_note: Note, *args, **kwargs) -> None:
        tk.Label.__init__(self, text=bound_note.get_name(), relief='ridge', *args, **kwargs)
        self.settings = settings
        self.note: Note = bound_note
        self.highlighted: bool = False

    def highlight_on(self) -> None:
        self.change_color(self.settings.colors.get('highl'))
        self.highlighted = True

    def highlight_off(self) -> None:
        self.change_color(self.settings.colors.get('bg'))
        self.highlighted = False

    def change_color(self, color_str: str) -> None:
        self.configure(bg=color_str)
