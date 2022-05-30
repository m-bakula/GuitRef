import re

from src.structure import constants


# FUNCTIONS FOR READING FROM constants
def get_all_names() -> list[str]:
    return constants.NOTE_NAMES


def get_interval_name(interval: int) -> str:
    return constants.INTERVALS_DICT.get(interval)


def args_from_pos(position: int) -> dict:
    if not valid_position(position):
        raise ValueError('Position invalid')
    else:
        result = constants.ALL_NOTES[position]
        res_dict = {'name': result[0], 'octave': result[1]}
        return res_dict


def read_file(filename: str) -> list[str]:
    """Loads contents from a text file"""
    with open(filename, encoding='utf-8', mode='r') as the_file:
        contents = the_file.readlines()
    return contents


# FUNCTIONS FOR ARGUMENT CHECKING:
def valid_octave(octave: int) -> bool:
    """Checks if the argument is a valid octave number"""
    if octave in constants.NOTE_OCTAVES:
        return True
    else:
        return False


def valid_name(name: str) -> bool:
    """Checks if the argument is a valid note name"""
    pattern = re.compile(r'''
    ^                      # string starts
    ([CDEFGAB])            # one of uppercase letters: C, D, E, F, G, A, B
    ((\#*$)|(b*$))         # any no of sharps (#) and end of string OR any no of flats (b) and end of string
    ''', re.VERBOSE)

    if re.search(pattern, name) is None:
        return False
    else:
        return True


def valid_position(position: int) -> bool:
    """Checks if the argument is a valid position (index of a note in ALL_NOTES)"""
    max_pos = len(constants.ALL_NOTES) - 1
    if position < 0 or position > max_pos:
        return False
    else:
        return True
