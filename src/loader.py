from src.structure import functions
from src.notes.abstr_note import AbstractNote


class Loader:
    """Mix-in class for loading and unloading scales/chords/keys from contents"""
    def __init_subclass__(cls):
        cls.loaded_objs = set()

    @classmethod
    def load_objects(cls, contents: list[str]) -> None:
        """A generic factory for creating notegroup objects from recipe contents (e.g. text files). Adds created objects
         to the loaded_objs set"""
        for a_line in contents:
            # TODO: proper failsafe (regex) for not matching patterns
            if a_line[0] == '#' or a_line[0] == '\n':
                pass
            else:
                label, *list_of_strings, = a_line.split()
                arg = [int(a_string) for a_string in list_of_strings]

                for a_name in functions.get_all_names():
                    full_label = a_name + label
                    new_obj = cls(AbstractNote(a_name), arg, full_label)
                    cls.loaded_objs.add(new_obj)

    @classmethod
    def unload_objects(cls) -> None:
        """Clears the loaded_objs set"""
        cls.loaded_objs.clear()

    @classmethod
    def get_objects(cls) -> set[AbstractNote]:
        """Returns the loaded_objs set"""
        return cls.loaded_objs
