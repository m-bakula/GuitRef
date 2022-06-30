from src.structure.constants import NOTE_NAMES
from src.structure.functions import valid_name


# FUNCTIONS FOR MANIPULATING NOTES:
def add_interval_abstr(start_note: str, interval: int) -> str:
    """Returns a note name that is an integer (possibly negative) of semitones apart from start_note"""
    if start_note not in NOTE_NAMES:
        raise ValueError('Starting note is not in NOTE_NAMES')
    else:
        position = (NOTE_NAMES.index(start_note) + interval) % len(NOTE_NAMES)
        return NOTE_NAMES[position]


def get_interval_abstr(root_name: str, target_name: str) -> int:
    """Returns a number of semitones needed to get from root note to target note (always positive)"""
    if root_name not in NOTE_NAMES or target_name not in NOTE_NAMES:
        raise ValueError('Root note is not in NOTE_NAMES')
    else:
        root_ind = NOTE_NAMES.index(root_name)
        target_ind = NOTE_NAMES.index(target_name)
        ind_diff = target_ind - root_ind

        if target_ind >= root_ind:
            return ind_diff
        else:
            return len(NOTE_NAMES) + ind_diff


def enh_name(a_name: str) -> str:
    """Returns a note name that is enharmonic (equivalent) to the argument but is in NOTE_NAMES. That name has at most
    one sharp/flat and can be compared to others in the list by index"""
    if not valid_name(a_name):
        raise ValueError('Not a valid note name - should be an uppercase letter (C-B), optionally followed by either \
                        sharps (#) or flats (b)')
    elif a_name in NOTE_NAMES:
        return a_name
    else:
        start_note = a_name[0]
        pos_deltas = {'b': -1, '#': 1}
        pos_change = 0

        for a_character in a_name:
            if a_character in pos_deltas.keys():
                pos_change += pos_deltas.get(a_character)

        return add_interval_abstr(start_note, pos_change)
