from src.guitar.string import String
from src.notegroup import NoteGroup
from src.notes.note_class import NoteClass
from src.notes.note import Note


class Fretboard:
    """Represents a fretboard with strings tuned to given notes and a given number of frets"""
    def __init__(self, fretnum: int, tuning: list[Note]) -> None:
        self.fretnum: int = fretnum
        self.tuning: list[Note] = [a_note for a_note in tuning]
        self.strings_list: list[String] = []

        self.update_fretboard()

    def update_fretboard(self):
        """"Fills the list of strings according to tuning and number of frets"""
        self.strings_list = [String(start_note, self.fretnum) for start_note in self.tuning]

    def get_tuning(self) -> list[Note]:
        """Returns the tuning of the fretboard, starting from the first string"""
        return self.tuning

    def get_strings(self) -> list[String]:
        """Returns the list of string objects in the fretboard"""
        return self.strings_list

    def get_str_num(self) -> int:
        """Returns the number of strings of the fretboard"""
        return len(self.strings_list)

    def get_note_at(self, str_num: int, fret_num: int) -> Note:
        """Returns the note at string str_num and fret fre_num"""
        return self.strings_list[str_num].get_note_at_fret(fret_num)

    def update_tuning(self, new_tuning: list[Note]):
        """Replaces the list of strings using a new tuning"""
        self.tuning = new_tuning
        self.update_fretboard()

    def update_fretnum(self, new_fretnum: int):
        """Replaces the list of strings using a new fret number"""
        self.fretnum = new_fretnum
        self.update_fretboard()

    def find_note(self, a_note: NoteClass) -> list[tuple[int, list[int]]]:
        """"Returns a list of tuples with string number and output of find_note(a_note) for each string"""
        all_notes: list = []

        for str_num, a_string in enumerate(self.strings_list):
            fret_nums = a_string.find_note(a_note)
            all_notes.append((str_num, fret_nums))
        return all_notes

    def find_notegroup(self, a_notegroup: NoteGroup) -> list[tuple[int, list[int]]]:
        """Merges outputs of find_note() for every note in a given notegroup and returns them as a single list"""
        output: list = []
        temp_list: list = []

        # TODO: make recursive later
        for a_note in a_notegroup.get_notes():
            temp_list.extend(self.find_note(a_note))

        for str_num in range(self.get_str_num()):
            str_list: list = []
            for a_tuple in temp_list:
                if a_tuple[0] == str_num:
                    str_list.extend(a_tuple[1])
            str_list.sort()
            output.append((str_num, str_list))

        return output
