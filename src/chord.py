from src.note_abstr import NoteAbstract
from src.notegroup import NoteGroup


class Chord(NoteGroup):
    def __init__(self, root: NoteAbstract, extensions: list[int], label: str = '') -> None:
        self.root: NoteAbstract = root
        self.extensions = extensions
        self.label: str = label
        self.notes: set = set()

        self.fill_notes()

    def fill_notes(self):
        self.notes.add(self.root)
        for a_number in self.extensions:
            self.notes.add(self.root.add_interval(a_number))

    def __repr__(self) -> str:
        return 'Chord: R={}, N={}, lab={}'.format(self.root, self.notes, self.label)

    def get_root(self) -> NoteAbstract:
        return self.root

    def get_notes(self) -> set[NoteAbstract]:
        return self.notes

    def add_note(self, new_note: NoteAbstract) -> None:
        """Adds a new note to the chord"""
        self.notes.add(new_note)

    def remove_note(self, removed_note: NoteAbstract) -> None:
        """Removes a note from the chord"""
        self.notes.remove(removed_note)
