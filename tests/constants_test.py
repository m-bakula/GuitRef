import unittest

from src.structure import constants

default_all_notes = [('C', 0), ('C#', 0), ('D', 0), ('Eb', 0), ('E', 0), ('F', 0), ('F#', 0), ('G', 0), ('G#', 0),
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

default_positions_dict = {'C': [0, 12, 24, 36, 48, 60, 72, 84], 'C#': [1, 13, 25, 37, 49, 61, 73, 85],
                          'D': [2, 14, 26, 38, 50, 62, 74, 86], 'Eb': [3, 15, 27, 39, 51, 63, 75, 87],
                          'E': [4, 16, 28, 40, 52, 64, 76, 88], 'F': [5, 17, 29, 41, 53, 65, 77, 89],
                          'F#': [6, 18, 30, 42, 54, 66, 78, 90], 'G': [7, 19, 31, 43, 55, 67, 79, 91],
                          'G#': [8, 20, 32, 44, 56, 68, 80, 92], 'A': [9, 21, 33, 45, 57, 69, 81, 93],
                          'Bb': [10, 22, 34, 46, 58, 70, 82, 94], 'B': [11, 23, 35, 47, 59, 71, 83, 95]}

sharps = ['', '#', '##', '###', '####', '#####', '######', '#######', '########', '#########',
          '##########', '###########', '############']
flats = ['', 'b', 'bb', 'bbb', 'bbbb', 'bbbbb', 'bbbbbb', 'bbbbbbb', 'bbbbbbbb', 'bbbbbbbbb',
         'bbbbbbbbbb', 'bbbbbbbbbbb', 'bbbbbbbbbbbb']
bad_args = ['Cd', 'Z', 'dZ', 'bZ', 'Zb', '#Z', 'Z#', 'C#b', 'Cb#', 'bCb#', '#Cb', 'bCbb#', '#Cbb']

enh_cases = {('C', sharps[1]): 'C#', ('C', sharps[2]): 'D', ('C', sharps[3]): 'Eb', ('C', sharps[4]): 'E',
             ('C', sharps[5]): 'F', ('C', sharps[6]): 'F#', ('C', sharps[7]): 'G', ('C', sharps[8]): 'G#',
             ('C', sharps[9]): 'A', ('C', sharps[10]): 'Bb', ('C', sharps[11]): 'B', ('C', sharps[12]): 'C',
             ('C', flats[1]): 'B', ('C', flats[2]): 'Bb', ('C', flats[3]): 'A', ('C', flats[4]): 'G#',
             ('C', flats[5]): 'G', ('C', flats[6]): 'F#', ('C', flats[7]): 'F', ('C', flats[8]): 'E',
             ('C', flats[9]): 'Eb', ('C', flats[10]): 'D', ('C', flats[11]): 'C#', ('C', flats[12]): 'C'}


class ConstantsTest(unittest.TestCase):
    def test_all_notes(self):
        """Test if default_all_notes matches constants.ALL_NOTES"""
        self.assertEqual(constants.ALL_NOTES, default_all_notes)

    def test_positions_dict(self):
        """Tests if default_positions_dict matches constants.POSITIONS_DICT"""
        self.assertEqual(constants.POSITIONS_DICT, default_positions_dict)

    def test_enh_name(self):
        """Tests if constants.enh_name returns correct results for enh_cases and raises ValueError for bad_args"""
        for arg_tuple in enh_cases.keys():
            arg = arg_tuple[0] + arg_tuple[1]
            self.assertEqual(constants.enh_name(arg), enh_cases.get(arg_tuple))

        for a_bad_arg in bad_args:
            with self.assertRaises(ValueError):
                constants.enh_name(a_bad_arg)


if __name__ == '__main__':
    unittest.main()
