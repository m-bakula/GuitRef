from src.notes.note_class import NoteClass
from src.structure.functions import args_from_pos
from src.structure.functions import valid_octave


class Note(NoteClass):
    """Represents a particular musical note in range given by ALL_NOTES, e.g. A2"""
    def __init__(self, name: str, octave: int) -> None:
        try:
            # will still initialize NoteClass if only octave is invalid
            NoteClass.__init__(self, name)
            if not valid_octave(octave):
                raise ValueError('Not a valid octave')
        except ValueError as error:
            raise error
        else:
            self.octave: int = octave
            self.position: int = self.position_list[octave]

    def __repr__(self) -> str:
        return self.name + str(self.octave) + ' (pos={})'.format(self.position)

    def __lt__(self, other: 'Note') -> bool:
        if self.position < other.position:
            return True
        else:
            return False

    def __eq__(self, other) -> bool:
        return self.is_equal(other)

    def __hash__(self) -> int:
        return hash(self.position)

    def get_octave(self) -> int:
        """Returns the note octave"""
        return self.octave

    def is_equal(self, other: 'Note') -> bool:
        """Extends NoteClass.is_equal to account for octaves"""
        if NoteClass.is_equal(self, other):
            return self.get_octave() == other.get_octave()
        else:
            return False

    def add_interval(self, interval: int) -> 'Note':
        """Replaces NoteClass.add_interval to account for octaves"""
        new_pos = self.position + interval
        args = (args_from_pos(new_pos).get('name'), args_from_pos(new_pos).get('octave'))
        return Note(*args)

    def get_interval(self, other: 'Note') -> int:
        """Replaces NoteClass.get_interval. Returns number of semitones from self to other note.
        Positive when going up, negative when down"""
        return other.position - self.position

    def to_abstract(self) -> NoteClass:
        """Returns the abstract note class of a given note"""
        return NoteClass(self.name)
