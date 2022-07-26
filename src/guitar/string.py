from typing import Iterable

from src.notes.note_class import NoteClass
from src.notes.note import Note


class String:
    """Represents a single string tuned to a particular note"""
    def __init__(self, tuned_to: Note, fretnum: int) -> None:
        try:
            self.fretnum: int = fretnum
            self.fret_range: Iterable = range(self.fretnum + 1)
            self.tuned_to: Note = tuned_to
            self.note_list: list[Note] = []
            
            for a_fret in self.fret_range:
                self.note_list.append(tuned_to.add_interval(a_fret))
        except ValueError as error:
            raise error

    def get_frets(self) -> int:
        """Returns the number of frets for the string"""
        return self.fretnum

    def get_range(self) -> Iterable[int]:
        """Returns a range object starting at 0 and ending at the last fret number"""
        return self.fret_range

    def get_notes(self) -> list[Note]:
        """Returns all notes on the string, ordered by fret number"""
        return self.note_list

    def get_note_at_fret(self, fret_num: int) -> Note:
        """Returns the note on the string at a given fret"""
        if fret_num not in self.fret_range:
            raise ValueError("Fret number can't be greater than the number of frets")
        else:
            return self.get_notes()[fret_num]

    def find_note(self, search_note: NoteClass) -> list[int]:
        """Returns the list of fret numbers where a note is on the string (possibly empty if it's not)"""
        output: list[int] = []

        if isinstance(search_note, Note):
            for num in self.fret_range:
                if self.get_notes()[num] == search_note:
                    output.append(num)
        else:
            for num in self.fret_range:
                if self.get_notes()[num].to_abstract() == search_note:
                    output.append(num)
        return output
