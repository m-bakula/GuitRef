from src.notegroup import NoteGroup
from src.notes.abstr_note import AbstractNote


class Scale(NoteGroup):
    def __init__(self, root: AbstractNote, intervals: list[int], label: str = '') -> None:
        self.root: AbstractNote = root
        self.intervals: list[int] = intervals
        self.label: str = label

        self.note_list: list = []
        self.note_list.append(self.root)
        current_note = self.root
        for an_interval in self.intervals:
            next_note = current_note.add_interval(an_interval)
            self.note_list.append(next_note)
            current_note = next_note

    def __repr__(self) -> str:
        return 'Scale: R={}, I={}, lab={}'.format(self.root, self.intervals, self.label)

    def get_root(self) -> AbstractNote:
        return self.root

    def get_notes(self) -> list[AbstractNote]:
        return self.note_list
