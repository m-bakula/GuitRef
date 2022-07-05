# define default values for gui
DEFAULT_FILE = ''
DEFAULT_BG = 'grey'
DEFAULT_HL = 'red'


class Settings:
    def __init__(self) -> None:
        self.file = DEFAULT_FILE
        # colors
        self.bg = DEFAULT_BG
        self.hl = DEFAULT_HL

    def load_settings(self) -> None:
        pass

    def save_settings(self) -> None:
        pass

    def change_setting(self, attr_name: str) -> None:
        pass
