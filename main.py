import os

from src.gui.window import Window
from src.structure.functions import read_file
from src.scale import Scale
from src.chord import Chord


scales_content = read_file(os.path.join('config', 'scales.txt'))
chords_content = read_file(os.path.join('config', 'chords.txt'))

Scale.load_objects(scales_content)
Chord.load_objects(chords_content)

main_window = Window()
main_window.mainloop()
