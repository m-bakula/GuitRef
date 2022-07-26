import unittest

from src.guitar.fretboard import Fretboard
from src.notegroup import NoteGroup
from src.notes.note_class import NoteClass
from src.notes.note import Note

test_fretboard = Fretboard(24, [Note('E', 4), Note('B', 3), Note('G', 3), Note('D', 3), Note('A', 2), Note('E', 2)])
test_notes_abstr = [NoteClass('E'), NoteClass('A')]
test_notes = [Note('A', 3), Note('E', 3)]


class ExampleNoteGroup(NoteGroup):
    def __init__(self, root: NoteClass, notes: list[NoteClass]):
        self.root: NoteClass = root
        self.notes: list[NoteClass] = notes

    def get_root(self) -> NoteClass:
        return self.root

    def get_notes(self) -> list[NoteClass]:
        return self.notes


test_notegroup = ExampleNoteGroup(test_notes_abstr[0], test_notes_abstr)


class FretboardTest(unittest.TestCase):
    def test_find_note(self):
        pass

    def test_find_notegroup(self):
        pass


if __name__ == '__main__':
    unittest.main()
