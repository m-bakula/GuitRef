from src.notes.abstr_note import AbstractNote
from src.notes.note import Note
from src.notegroup import NoteGroup
from src.guitar.string import String


class Fretboard:
    """Represents a fretboard with strings tuned to given notes and a given number of frets"""
    def __init__(self, fretnum: int, tuning: list[Note]) -> None:
        self.fretnum: int = fretnum
        self.tuning: list[str] = [str(a_note) for a_note in tuning]
        self.strings_list: list[String] = [String(start_note, fretnum) for start_note in tuning]

    def get_frets(self):
        return self.fretnum

    def get_tuning(self):
        return self.tuning

    def find_note(self, a_note: AbstractNote) -> list[tuple[int, list[int]]]:
        all_notes = []
        for a_string in self.strings_list:
            str_num = self.strings_list.index(a_string)
            fret_nums = a_string.find_note_str(a_note)
            all_notes.append((str_num, fret_nums))

        return all_notes

    def get_note_at(self, str_num: int, fret_num: int) -> Note:
        return self.strings_list[str_num].get_note_at_fret(fret_num)

    def change_tuning(self, new_tuning: list[Note]):
        pass

    def change_frets(self, new_fretnum: int):
        pass

    def find_notegroup(self, a_notegroup: NoteGroup):
        pass
