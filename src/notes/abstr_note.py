from src.structure.constants import POSITIONS_DICT
from src.structure.functions import valid_name
from src.structure.note_functions import add_interval_abstr
from src.structure.note_functions import enh_name
from src.structure.note_functions import get_interval_abstr


class AbstractNote:
    """Represents a single note class, e.g. C"""
    def __init__(self, name: str) -> None:
        try:
            if not valid_name(name):
                raise ValueError('Not a valid note name')
        except ValueError as error:
            raise error
        else:
            self.name: str = name
            self.enh_name: str = enh_name(name)
            self.position_list: list[int] = POSITIONS_DICT[self.name]

    def __repr__(self) -> str:
        return self.name + ' (abstr)'

    def __eq__(self, other) -> bool:
        return self.is_equal(other)

    def __hash__(self) -> int:
        return hash(self.enh_name)

    def is_equal(self, other) -> bool:
        """Checks if other is the same (enharmonic) to self"""
        return self.enh_name == other.enh_name

    def add_interval(self, interval: int) -> 'AbstractNote':
        """Returns abstract note that is an integer (can be non-positive) of semitones apart from self"""
        new_name = add_interval_abstr(self.name, interval)
        return AbstractNote(new_name)

    def get_interval(self, other) -> int:
        """Returns a number of semitones needed to get from self to other (always positive)"""
        return get_interval_abstr(self.enh_name, other.enh_name)

    def get_all_pos(self) -> list[int]:
        """Returns a list of all positions of notes of a given class in range"""
        return self.position_list
