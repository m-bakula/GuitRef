import os
import pickle

from src.gui.window import Window
from settings import Settings

SETTS_LOCATION = 'settings.pickle'


def load_settings(filepath: str = SETTS_LOCATION) -> Settings:
    if os.path.exists(filepath):
        with open(filepath, 'rb') as setts_file:
            loaded_settings = pickle.load(setts_file)
    else:
        loaded_settings = Settings()
    return loaded_settings


def save_settings(settings: Settings, filepath: str = SETTS_LOCATION) -> None:
    with open(filepath, 'wb') as setts_file:
        pickle.dump(settings, setts_file)


main_window = Window(settings=load_settings())
main_window.mainloop()
save_settings(main_window.settings)
