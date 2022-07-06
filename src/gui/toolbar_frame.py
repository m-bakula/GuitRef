import tkinter as tk


class ToolbarFrame(tk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        tk.Frame.__init__(self, *args, **kwargs)
        self.btn_quit = None
        self.btn_options = None

        self.create_widgets()
        self.configure_grid()

    def create_widgets(self) -> None:
        self.btn_quit = tk.Button(master=self, text='Quit')
        self.btn_options = tk.Button(master=self, text='Options')

    def configure_grid(self) -> None:
        self.btn_options.grid(row=0, column=0)
        self.btn_quit.grid(row=0, column=1)
