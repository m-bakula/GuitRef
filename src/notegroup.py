from abc import ABC
from abc import abstractmethod
from typing import Iterable

from src.loader import Loader
from src.notes.abstr_note import AbstractNote
from src.notes.note import Note
from src.structure.functions import get_interval_name


class NoteGroup(ABC, Loader):
    """An abstract base class for objects containing multiple notes: scales, chords, keys"""
    @abstractmethod
    def get_root(self) -> AbstractNote:
        """Should return the root note of a notegroup"""
        raise NotImplementedError

    @abstractmethod
    def get_notes(self) -> Iterable[AbstractNote]:
        """Should return all notes of a notegroup as a list"""
        raise NotImplementedError

    def get_notes_abstr(self) -> set[AbstractNote]:
        """Returns a set of abstract note classes of all notes in get_notes()"""
        abstr_set = set()
        for a_note in self.get_notes():
            if isinstance(a_note, AbstractNote) and not isinstance(a_note, Note):
                abstr_set.add(a_note)
            elif isinstance(a_note, Note):
                abstr_set.add(a_note.to_abstract())
        return abstr_set

    def is_enharmonic_to(self, other) -> bool:
        """Checks whether notegroups are enharmonic (have all the same abstract notes)"""
        return self.get_notes_abstr() == other.get_notes_abstr()

    def interval_list(self) -> list[tuple[int, str]]:
        """Returns intervals relative to the root of all abstract notes contained in the notegroup"""
        interval_list = []
        for a_note in self.get_notes_abstr():
            interval_list.append(self.get_root().get_interval(a_note))

        interval_list.sort()
        results_list = [(interval, get_interval_name(interval)) for interval in interval_list]
        return results_list
