import tkinter as tk

from src.structure.constants import NOTE_NAMES
from src.chord import Chord
from src.scale import Scale
# to be deleted
from src.structure.functions import read_file
import os.path


class SelectionFrame(tk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        Scale.load_recipes(read_file(os.path.join('config', 'scales.txt')))
        tk.Frame.__init__(self, *args, **kwargs)
        self.selected_name = None
        self.drop_name = None

        self.selected_recipe = None
        self.drop_recipe = None

        self.btn_show = None
        self.btn_hide = None
        self.lbl_txt = None

        self.create_widgets()
        self.configure_grid()

    def create_widgets(self):
        name_list = NOTE_NAMES
        var_name = tk.StringVar(self)
        self.drop_name = tk.OptionMenu(self, var_name, *name_list)

        recipes = [a_recipe[0] for a_recipe in Scale.get_recipes()]
        var_rec = tk.StringVar(self)
        self.drop_recipe = tk.OptionMenu(self, var_rec, *recipes)

    def configure_grid(self):
        self.drop_name.grid(row=0, column=0)
        self.drop_recipe.grid(row=0, column=1)

    def select_name(self):
        pass

    def select_recipe(self):
        pass

    def show(self):
        if self.selected_name is not None and self.selected_recipe is not None:
            pass
            # make selected object
            # and highlight it
