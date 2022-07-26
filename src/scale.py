from src.note_abstr import NoteAbstract
from src.notegroup import NoteGroup


class Scale(NoteGroup):
    def __init__(self, root: NoteAbstract, intervals: list[int], label: str = '') -> None:
        self.root: NoteAbstract = root
        self.intervals: list[int] = intervals
        self.label: str = label
        self.note_list: list = []

        self.fill_note_list()

    def fill_note_list(self):
        self.note_list.append(self.root)
        current_note = self.root
        for an_interval in self.intervals:
            next_note = current_note.add_interval(an_interval)
            self.note_list.append(next_note)
            current_note = next_note

    def __repr__(self) -> str:
        return 'Scale: R={}, I={}, lab={}'.format(self.root, self.intervals, self.label)

    def get_root(self) -> NoteAbstract:
        return self.root

    def get_notes(self) -> list[NoteAbstract]:
        return self.note_list
