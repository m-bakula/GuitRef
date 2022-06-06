import unittest

from src.notes.abstr_note import AbstractNote


class AbstrNoteTest(unittest.TestCase):
    pos_dict = {'C': [0, 12, 24, 36, 48, 60, 72, 84], 'C#': [1, 13, 25, 37, 49, 61, 73, 85],
                'D': [2, 14, 26, 38, 50, 62, 74, 86], 'Eb': [3, 15, 27, 39, 51, 63, 75, 87],
                'E': [4, 16, 28, 40, 52, 64, 76, 88], 'F': [5, 17, 29, 41, 53, 65, 77, 89],
                'F#': [6, 18, 30, 42, 54, 66, 78, 90], 'G': [7, 19, 31, 43, 55, 67, 79, 91],
                'G#': [8, 20, 32, 44, 56, 68, 80, 92], 'A': [9, 21, 33, 45, 57, 69, 81, 93],
                'Bb': [10, 22, 34, 46, 58, 70, 82, 94], 'B': [11, 23, 35, 47, 59, 71, 83, 95]}

    test_dict = {('C', 1): 'C#', ('C', 2): 'D', ('C', 3): 'Eb', ('C', 4): 'E', ('C', 5): 'F', ('C', 6): 'F#',
                 ('C', 7): 'G', ('C', 8): 'G#', ('C', 9): 'A', ('C', 10): 'Bb', ('C', 11): 'B', ('C', 12): 'C',
                 ('C', -1): 'B', ('C', -2): 'Bb', ('C', -3): 'A', ('C', -4): 'G#', ('C', -5): 'G', ('C', -6): 'F#',
                 ('C', -7): 'F', ('C', -8): 'E', ('C', -9): 'Eb', ('C', -10): 'D', ('C', -11): 'C#', ('C', 12): 'C'}

    test_abstr_dict = {('C', 'C#'): 1, ('C', 'D'): 2, ('C', 'Eb'): 3, ('C', 'E'): 4, ('C', 'F'): 5, ('C', 'F#'): 6,
                       ('C', 'G'): 7, ('C', 'G#'): 8, ('C', 'A'): 9, ('C', 'Bb'): 10, ('C', 'B'): 11, ('C', 'C'): 0}

    def test_abstr_notes(self):
        """Tests if AbstractNote objects are properly instantiated"""
        for a_key in AbstrNoteTest.pos_dict.keys():
            abs_note = AbstractNote(a_key)
            self.assertEqual(abs_note.position_list, AbstrNoteTest.pos_dict.get(a_key))

    def test_add_interval(self):
        """Tests for all combinations of adding intervals to a note"""
        for a_tuple in AbstrNoteTest.test_dict.keys():
            good_value = AbstrNoteTest.test_dict.get(a_tuple)
            start_note, test_interval = AbstractNote(a_tuple[0]), a_tuple[1]
            test_value = start_note.add_interval(test_interval).name
            self.assertEqual(test_value, good_value)

    def test_get_interval(self):
        """Tests all abstract note pairs for getting the correct interval"""
        for a_tuple in AbstrNoteTest.test_abstr_dict.keys():
            root_note = AbstractNote(a_tuple[0])
            target_note = AbstractNote(a_tuple[1])
            value = AbstrNoteTest.test_abstr_dict.get(a_tuple)
            self.assertEqual(root_note.get_interval(target_note), value)


if __name__ == '__main__':
    unittest.main()
