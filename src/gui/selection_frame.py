import tkinter as tk

from settings import Settings
from src.chord import Chord
from src.gui.fretboard_frame import FretboardFrame
from src.gui.label_frame import LabelFrame
from src.notes.abstr_note import AbstractNote
from src.scale import Scale
from src.structure.constants import NOTE_NAMES


class SelectionFrame(tk.Frame):
    def __init__(self,
                 settings: Settings,
                 fretboard_frame: FretboardFrame,
                 label_frame: LabelFrame,
                 *args, **kwargs) -> None:
        tk.Frame.__init__(self, *args, **kwargs)
        self.settings = settings
        Scale.load_recipes(self.settings.scales)
        Chord.load_recipes(self.settings.chords)
        self.fretboard_frame = fretboard_frame
        self.label_frame = label_frame

        self.menu_name = None
        self.name_init = 'Select note'
        self.select_name = tk.StringVar(master=self, value=self.name_init)

        self.menu_recipe = None
        self.recipe_init = 'Select scale'
        self.select_recipe = tk.StringVar(master=self, value='Select scale')

        self.btn_show = None
        self.btn_hide = None
        self.lbl_txt = None

        self.create_widgets()
        self.configure_grid()

    def create_widgets(self):
        name_list = NOTE_NAMES
        self.menu_name = tk.OptionMenu(self, self.select_name, *name_list)

        recipe_labels = Scale.get_recipes().keys()
        self.menu_recipe = tk.OptionMenu(self, self.select_recipe, *recipe_labels)

        self.btn_show = tk.Button(master=self, text='Show', command=self.show)
        self.btn_hide = tk.Button(master=self, text='Hide', command=self.hide)
        self.lbl_txt = tk.Label(master=self, text='SCALES')

    def configure_grid(self):
        self.lbl_txt.grid(row=0, columnspan=2)
        self.menu_name.grid(row=1, column=0)
        self.menu_recipe.grid(row=1, column=1)
        self.btn_show.grid(row=2, column=0)
        self.btn_hide.grid(row=2, column=1)

    def show(self):
        selected_name = self.select_name.get()
        selected_recipe = self.select_recipe.get()
        label = selected_name + selected_recipe

        if selected_name != self.name_init and selected_recipe != self.recipe_init:
            root = AbstractNote(selected_name)
            intervals = Scale.get_recipes().get(selected_recipe)
            obj_to_show = Scale(root, intervals, label)
            self.fretboard_frame.highlight_object(obj_to_show)
            self.label_frame.make_visible(label)

    def hide(self):
        self.fretboard_frame.remove_highlight()
        self.label_frame.make_invisible()
