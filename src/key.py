from src.notes.abstr_note import AbstractNote
from src import notegroup, scale, chord


class Key(notegroup.NoteGroup):
    def __init__(self):
        self.root = ''
        self.signature = (0, None)
        self.chords = dict()
        self.notes = set()

    def __repr__(self):
        # TODO: implement
        return ''

    def get_root(self):
        return self.root

    def get_notes(self) -> list[AbstractNote]:
        return list(self.notes)

    def get_sig(self) -> tuple[int, str]:
        return self.signature

    def get_chords(self) -> set[chord.Chord]:
        return set(self.chords)

    def to_scale(self) -> scale.Scale:
        pass

    def has_chord(self, a_chord: chord.Chord) -> bool:
        pass
