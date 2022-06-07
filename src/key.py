from src.notes.abstr_note import AbstractNote
from src.notegroup import NoteGroup
from src.scale import Scale
from src.chord import Chord
from src.key_dict import KeyDict


class Key(NoteGroup):
    def __init__(self, root: AbstractNote, key_dict: KeyDict):
        self.root = root
        self.signature = (0, None)
        self.chords = dict()
        self.notes = set()

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
        return set(self.chords)

    def to_scale(self) -> Scale:
        pass

    def has_chord(self, a_chord: Chord) -> bool:
        pass
