import tkinter as tk


class TlbrFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.create_widgets()
        self.configure_grid()
        self.btn_quit = None

    def create_widgets(self):
        self.btn_quit = tk.Button(master=self, text='Quit')

    def configure_grid(self):
        self.btn_quit.grid(row=0, column=0)
