import tkinter as tk

from src.gui.gtr_frame import GtrFrame
from src.gui.tlbr_frame import TlbrFrame


class Window(tk.Tk):
    def __init__(self,):
        tk.Tk.__init__(self)
        self.title('GuitRef')
        self.frm_gtr: GtrFrame = GtrFrame(master=self)
        self.frm_tlbr: TlbrFrame = TlbrFrame(master=self)

        self.configure_grid()
        self.manage_frames()

    def configure_grid(self):
        self.columnconfigure(0, minsize=400)
        self.rowconfigure([0, 1], minsize=200)

    def manage_frames(self):
        self.frm_gtr.grid(row=0, column=0)
        self.frm_tlbr.grid(row=1, column=0)
