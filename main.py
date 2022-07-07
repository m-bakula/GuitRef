import os

from settings import Settings
from src.gui.window import Window

current_settings = Settings()

if os.path.exists('settings.pickle'):
    current_settings.load_settings()
else:
    current_settings.save_settings()

main_window = Window()
main_window.mainloop()
