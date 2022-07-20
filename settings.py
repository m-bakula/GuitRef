import os

from src.structure.functions import read_file


# define default values for settings
DEFAULT_FILE = ''
DEFAULT_COLORS = {'fg': 'black', 'bg': 'grey', 'highl': 'red'}
DEFAULT_FONT = {'font': 'Arial', 'big': 24, 'med_big': 20, 'med_small': 16, 'small': 12}
DEFAULT_SCALES = read_file(os.path.join('config', 'scales.txt'))
DEFAULT_CHORDS = read_file(os.path.join('config', 'chords.txt'))


class Settings:
    def __init__(self,
                 file=DEFAULT_FILE,
                 scales=DEFAULT_SCALES,
                 chords=DEFAULT_CHORDS,
                 colors=DEFAULT_COLORS,
                 font=DEFAULT_FONT,
                 ) -> None:
        self.file = file
        self.scales = scales
        self.chords = chords
        self.font = font
        self.colors = colors

    def load_settings(self) -> None:
        pass

    def save_settings(self) -> None:
        pass

    def change_setting(self, attr_name: str) -> None:
        pass
