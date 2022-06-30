import unittest

from src.notes.note import Note
from src.structure.constants import ALL_NOTES


class NoteTest(unittest.TestCase):
    arg_list = [('C', 0), ('C#', 0), ('D', 0), ('Eb', 0), ('E', 0), ('F', 0), ('F#', 0), ('G', 0), ('G#', 0),
                ('A', 0), ('Bb', 0), ('B', 0), ('C', 1), ('C#', 1), ('D', 1), ('Eb', 1), ('E', 1), ('F', 1),
                ('F#', 1), ('G', 1), ('G#', 1), ('A', 1), ('Bb', 1), ('B', 1), ('C', 2), ('C#', 2), ('D', 2),
                ('Eb', 2), ('E', 2), ('F', 2), ('F#', 2), ('G', 2), ('G#', 2), ('A', 2), ('Bb', 2), ('B', 2),
                ('C', 3), ('C#', 3), ('D', 3), ('Eb', 3), ('E', 3), ('F', 3), ('F#', 3), ('G', 3), ('G#', 3),
                ('A', 3), ('Bb', 3), ('B', 3), ('C', 4), ('C#', 4), ('D', 4), ('Eb', 4), ('E', 4), ('F', 4),
                ('F#', 4), ('G', 4), ('G#', 4), ('A', 4), ('Bb', 4), ('B', 4), ('C', 5), ('C#', 5), ('D', 5),
                ('Eb', 5), ('E', 5), ('F', 5), ('F#', 5), ('G', 5), ('G#', 5), ('A', 5), ('Bb', 5), ('B', 5),
                ('C', 6), ('C#', 6), ('D', 6), ('Eb', 6), ('E', 6), ('F', 6), ('F#', 6), ('G', 6), ('G#', 6),
                ('A', 6), ('Bb', 6), ('B', 6), ('C', 7), ('C#', 7), ('D', 7), ('Eb', 7), ('E', 7), ('F', 7),
                ('F#', 7), ('G', 7), ('G#', 7), ('A', 7), ('Bb', 7), ('B', 7)]

    bad_arg_list = [('a', 0), ('H', 0), ('B', 9), ('B', -7)]

    def test_notes(self):
        """Tests if Note objects are properly instantiated"""
        for a_tuple in NoteTest.arg_list:
            a_note = Note(*a_tuple)
            self.assertEqual(a_note.position, NoteTest.arg_list.index(a_tuple))

        for a_tuple in NoteTest.bad_arg_list:
            with self.assertRaises(ValueError):
                Note(*a_tuple)

    def test_add_interval(self):
        """Tests adding intervals for all note combinations, should raise ValueError when
        result not in ALL_NOTES"""
        all_notes_len = len(ALL_NOTES)

        for a_tuple in NoteTest.arg_list:
            a_note = Note(*a_tuple)
            tuple_index = NoteTest.arg_list.index(a_tuple)
            for a_number in range(-all_notes_len, all_notes_len):
                if 0 <= tuple_index + a_number < all_notes_len:
                    target_note = a_note.add_interval(a_number)
                    good_note = NoteTest.arg_list[tuple_index + a_number]
                    # see if target note is the same as expected, according to arg_list
                    self.assertEqual((target_note.name, target_note.octave), (good_note[0], good_note[1]))
                else:
                    # see if a_note.add_interval(a_number) raises ValErr
                    with self.assertRaises(ValueError):
                        a_note.add_interval(a_number)

    def test_get_interval(self):
        """Tests getting intervals for all note combinations"""
        for tuple_start in NoteTest.arg_list:
            index_start = NoteTest.arg_list.index(tuple_start)
            note_start = Note(*tuple_start)
            for tuple_target in NoteTest.arg_list:
                index_target = NoteTest.arg_list.index(tuple_target)
                note_target = Note(*tuple_target)
                self.assertEqual(index_target - index_start, note_start.get_interval(note_target))

    def test_comparisons(self):
        """Tests all cases of comparing with __lt__, will guarantee that is_equal and __eq__ work correctly"""
        for tuple_start in NoteTest.arg_list:
            index_start = NoteTest.arg_list.index(tuple_start)
            note_start = Note(*tuple_start)
            for tuple_target in NoteTest.arg_list:
                index_target = NoteTest.arg_list.index(tuple_target)
                note_target = Note(*tuple_target)
                self.assertEqual(note_start.__lt__(note_target), index_start < index_target)


if __name__ == '__main__':
    unittest.main()
