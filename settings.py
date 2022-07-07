import os

from src.structure.functions import read_file


# define default values for settings
DEFAULT_FILE = ''
DEFAULT_BG = 'grey'
DEFAULT_HL = 'red'
DEFAULT_SCALES = read_file(os.path.join('config', 'scales.txt'))
DEFAULT_CHORDS = read_file(os.path.join('config', 'chords.txt'))


class Settings:
    def __init__(self,
                 file=DEFAULT_FILE,
                 scales=DEFAULT_SCALES,
                 chords=DEFAULT_CHORDS,
                 background=DEFAULT_BG,
                 highlight=DEFAULT_HL,
                 ) -> None:
        self.file = file
        self.scales = scales
        self.chords = chords
        # colors
        self.bg = background
        self.hl = highlight

    def load_settings(self) -> None:
        pass

    def save_settings(self) -> None:
        pass

    def change_setting(self, attr_name: str) -> None:
        pass
