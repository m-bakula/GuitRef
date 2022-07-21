import os
from pickle import dump

from src.guitar.fretboard import Fretboard
from src.notes.note import Note
from src.structure.functions import read_file

# define default values for settings
DEFAULT_COLORS = {'fg': 'black', 'bg': 'light grey', 'highl': 'orange red'}
DEFAULT_FONT = {'font': 'Arial', 'big': 24, 'med_big': 20, 'med_small': 16, 'small': 12}
DEFAULT_SCALES = read_file(os.path.join('config', 'scales.txt'))
DEFAULT_CHORDS = read_file(os.path.join('config', 'chords.txt'))
DEFAULT_FRETBOARD = Fretboard(24, [Note('D', 4), Note('B', 3), Note('G', 3), Note('D', 3), Note('A', 2),
                                   Note('E', 2)])


class Settings:
    def __init__(self,
                 scales=DEFAULT_SCALES,
                 chords=DEFAULT_CHORDS,
                 colors=DEFAULT_COLORS,
                 font=DEFAULT_FONT,
                 fretboard=DEFAULT_FRETBOARD
                 ) -> None:
        self.scales: list[str] = scales
        self.chords: list[str] = chords
        self.font: dict = font
        self.colors: dict = colors
        self.fretbrd: Fretboard = fretboard
