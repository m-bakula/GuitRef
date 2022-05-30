import os

from src.structure.functions import read_file
from src.scale import Scale
from src.chord import Chord
from src.key import Key


scales_content = read_file(os.path.join('config', 'scales.txt'))
chords_content = read_file(os.path.join('config', 'chords.txt'))
keys_content = read_file(os.path.join('config', 'keys.txt'))

Scale.load_objects(scales_content)
Chord.load_objects(chords_content)

print(Scale.get_objects(), '\n')
print(Chord.get_objects(), '\n')
