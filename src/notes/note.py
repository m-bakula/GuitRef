from src.structure import functions
from src.notes.abstr_note import AbstractNote


class Note(AbstractNote):
    """Represents a particular musical note in range given by ALL_NOTES, e.g. A2"""
    def __init__(self, name: str, octave: int) -> None:
        try:
            # will still initialize AbstractNote if only octave is invalid
            AbstractNote.__init__(self, name)
            if not functions.valid_octave(octave):
                raise ValueError('Not a valid octave')
        except ValueError as error:
            raise error
        else:
            self.octave: int = octave
            self.position: int = self.position_list[octave]

    def __repr__(self) -> str:
        return self.name + str(self.octave) + ' (pos={})'.format(self.position)

    def __lt__(self, other) -> bool:
        if self.position < other.position:
            return True
        else:
            return False

    def __eq__(self, other) -> bool:
        return self.is_equal(other)

    def __hash__(self) -> int:
        return hash(self.position)

    def is_equal(self, other) -> bool:
        """Extends AbstractNote.is_equal to account for octaves"""
        if AbstractNote.is_equal(self, other):
            return self.octave == other.octave
        else:
            return False

    def add_interval(self, interval: int) -> 'Note':
        """Replaces AbstractNote.add_interval to account for octaves"""
        new_pos = self.position + interval
        args = (functions.args_from_pos(new_pos).get('name'), functions.args_from_pos(new_pos).get('octave'))
        return Note(*args)

    def get_interval(self, other) -> int:
        """Replaces AbstractNote.get_interval. Returns number of semitones from self to other note.
        Positive when going up, negative when down"""
        return other.position - self.position

    def to_abstract(self) -> AbstractNote:
        """Returns the abstract note class of a given note"""
        return AbstractNote(self.name)
