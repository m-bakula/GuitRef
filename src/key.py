from src.notes.abstr_note import AbstractNote
from src.notegroup import NoteGroup
from src.scale import Scale
from src.chord import Chord


class Key(NoteGroup):
    def __init__(self, root: AbstractNote, chord_list: list[Chord]):
        self.root = root
        self.signature = (0, None)
        self.chords = {a_num: chord_list[a_num] for a_num in range(0, len(chord_list))}
        self.notes = set()

        for a_chord in self.chords:
            self.notes.union({a_note for a_note in a_chord})

    def __repr__(self):
        # TODO: implement
        return ''

    def get_root(self):
        return self.root

    def get_notes(self) -> set[AbstractNote]:
        return self.notes

    def get_sig(self) -> tuple[int, str]:
        return self.signature

    def get_chords(self) -> set[Chord]:
        return self.chords.values()

    def to_scale(self) -> Scale:
        pass

    def has_chord(self, a_chord: Chord) -> bool:
        pass
