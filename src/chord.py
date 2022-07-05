from src.notegroup import NoteGroup
from src.notes.abstr_note import AbstractNote


class Chord(NoteGroup):
    def __init__(self, root: AbstractNote, extensions: list[int], label: str = '') -> None:
        self.root: AbstractNote = root
        self.label: str = label

        self.notes: set = set()
        self.notes.add(root)
        for a_number in extensions:
            self.notes.add(self.root.add_interval(a_number))

    def __repr__(self) -> str:
        return 'Chord: R={}, N={}, lab={}'.format(self.root, self.notes, self.label)

    def get_root(self) -> AbstractNote:
        return self.root

    def get_notes(self) -> set[AbstractNote]:
        return self.notes

    def add_note(self, new_note: AbstractNote) -> None:
        """Adds a new note to the chord"""
        self.notes.add(new_note)

    def remove_note(self, removed_note: AbstractNote) -> None:
        """Removes a note from the chord"""
        self.notes.remove(removed_note)
