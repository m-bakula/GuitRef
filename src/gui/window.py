import tkinter as tk

from src.gui.fretboard_frame import FretboardFrame
from src.gui.selection_frame import SelectionFrame
from src.gui.toolbar_frame import ToolbarFrame


class Window(tk.Tk):
    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.title('GuitRef')
        self.frm_gtr: FretboardFrame = FretboardFrame(master=self)
        self.frm_tlbr: ToolbarFrame = ToolbarFrame(master=self)
        self.frm_slct: SelectionFrame = SelectionFrame(master=self)

        self.configure_grid()
        self.manage_frames()

    def configure_grid(self) -> None:
        self.columnconfigure(0, minsize=400, weight=1)
        self.columnconfigure(1, minsize=200, weight=1)
        self.rowconfigure([0, 1], minsize=200, weight=1)

    def manage_frames(self) -> None:
        self.frm_gtr.grid(row=0, column=0,)
        self.frm_tlbr.grid(row=1, column=0)
        self.frm_slct.grid(row=0, column=1)
