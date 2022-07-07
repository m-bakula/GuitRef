import tkinter as tk

from src.notegroup import NoteGroup


class NoteGroupFrame(tk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        tk.Frame.__init__(self, *args, **kwargs)
        self.selected_notegroup = None
        self.drp_menu = None
        self.btn_show = None
        self.btn_hide = None

        self.create_widgets()
        self.configure_grid()

    def create_widgets(self):
        pass
        # self.drp_menu = tk.OptionMenu(master=self, text='test')

    def configure_grid(self):
        pass
        # self.drp_menu.grid(row=0, column=0)
