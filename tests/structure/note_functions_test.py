import unittest

from src.structure import note_functions

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


class NoteFunctionsTest(unittest.TestCase):
    def test_add_interval_abstr(self):
        pass

    def test_get_interval_abstr(self):
        pass

    def test_enh_name(self):
        """Tests if constants.enh_name returns correct results for enh_cases and raises ValueError for bad_args"""
        for arg_tuple in enh_cases.keys():
            arg = arg_tuple[0] + arg_tuple[1]
            self.assertEqual(note_functions.enh_name(arg), enh_cases.get(arg_tuple))

        for an_arg in bad_args:
            with self.assertRaises(ValueError):
                note_functions.enh_name(an_arg)


if __name__ == '__main__':
    unittest.main()
