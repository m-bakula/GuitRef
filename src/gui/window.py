import tkinter as tk

from settings import Settings
from src.gui.fretboard_frame import FretboardFrame
from src.gui.label_frame import LabelFrame
from src.gui.selection_frame import SelectionFrame
from src.gui.toolbar_frame import ToolbarFrame


class Window(tk.Tk):
    def __init__(self, settings: Settings) -> None:
        tk.Tk.__init__(self)
        self.settings: Settings = settings
        self.settings.colors['bg'] = self.cget('bg')
        self.title('GuitRef')
        self.frm_fretbrd: FretboardFrame = FretboardFrame(master=self,
                                                          settings=self.settings,
                                                          init_fretbrd=self.settings.fretbrd)
        self.frm_tlbr: ToolbarFrame = ToolbarFrame(master=self,
                                                   settings=self.settings)
        self.frm_label: LabelFrame = LabelFrame(master=self,
                                                settings=self.settings)
        self.frm_slct: SelectionFrame = SelectionFrame(master=self,
                                                       settings=self.settings,
                                                       fretboard_frame=self.frm_fretbrd,
                                                       label_frame=self.frm_label)

        self.configure(bg=settings.colors.get('bg'))
        self.configure_grid()
        self.manage_frames()

    def configure_grid(self) -> None:
        self.columnconfigure([0, 1], minsize=300, weight=1)
        self.columnconfigure(2, minsize=100, weight=1)
        self.rowconfigure([1, 2], minsize=200, weight=1)

    def manage_frames(self) -> None:
        self.frm_label.grid(row=0, column=0)
        self.frm_fretbrd.grid(row=1, column=0)
        self.frm_tlbr.grid(row=2, column=0)
        self.frm_slct.grid(row=1, column=1)
