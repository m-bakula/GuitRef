import unittest

from src import notegroup
from src.notes import note
from src.structure.constants import NOTE_NAMES


class ExampleClass(notegroup.NoteGroup):
    def __init__(self, root, args, label):
        self.root = root
        self.args = args
        self.label = label

    def __repr__(self):
        return self.label + ' ' + str(self.args)

    def get_root(self):
        return self.root

    def get_notes(self):
        note_list = [note.Note(a_name, 1) for a_name in NOTE_NAMES]
        return note_list


example_object = ExampleClass(note.Note('C', 1), [1, 2, 3], 'test')


class NoteGroupTest(unittest.TestCase):
    def test_load_unload(self):
        """Tests if objects are properly loaded and unloaded"""
        test_lines = ['maj 2 2 1 2 2 2', 'test 1 2 3 4 5 6 7 8 9', 'blank 0']
        results_dict = {}

        ExampleClass.load_recipes(test_lines)

        # fill out the results_dict with correct results
        for a_line in test_lines:
            label, *strings_list, = a_line.split()
            args_list = [int(string) for string in strings_list]
            labels_list = [name + label for name in NOTE_NAMES]
            results_dict[a_line] = [(a_label, args_list) for a_label in labels_list]

        # create a list of tuples with appropriate labels and args from results_dict
        all_values = []
        for value_list in results_dict.values():
            all_values += value_list

        # assert that every object has a tuple of attributes corresponding to one in all_values
        for an_object in ExampleClass.loaded_recipes:
            self.assertIsInstance(an_object, ExampleClass)
            test_pair = (an_object.label, an_object.args)
            self.assertIn(test_pair, all_values)

        ExampleClass.unload_objects()
        self.assertEqual(ExampleClass.loaded_recipes, set())

    def test_get_notes_abstr(self):
        """Tests get_notes_abstr method using a dummy subclass of notegroup"""
        abstr_set = set([note.AbstractNote(a_name) for a_name in NOTE_NAMES])
        self.assertEqual(abstr_set, example_object.get_notes_abstr())

    def test_is_enh(self):
        """Tests is_enharmonic_to method using a dummy subclass of notegroup"""
        example_object_2 = ExampleClass(note.Note('D', 1), [1, 2, 5, 9], 'test2')
        self.assertEqual(example_object.is_enharmonic_to(example_object_2), True)
        self.assertEqual(example_object_2.is_enharmonic_to(example_object), True)


if __name__ == '__main__':
    unittest.main()
