from src.guitar.string import String
from src.notegroup import NoteGroup
from src.notes.abstr_note import AbstractNote
from src.notes.note import Note


class Fretboard:
    """Represents a fretboard with strings tuned to given notes and a given number of frets"""
    def __init__(self, fretnum: int, tuning: list[Note]) -> None:
        self.fretnum: int = fretnum
        self.tuning: list[Note] = [a_note for a_note in tuning]
        self.strings_list: list[String] = []
        self.dict: dict[tuple[int, int], Note] = dict()

        self.update_tuning(self.tuning)

    def get_frets(self) -> int:
        return self.fretnum

    def get_tuning(self) -> list[Note]:
        return self.tuning

    def get_strings(self) -> list[String]:
        return self.strings_list

    def get_note_at(self, str_num: int, fret_num: int) -> Note:
        return self.strings_list[str_num].get_note_at_fret(fret_num)

    def update_fretboard(self, tuning: list[Note], fretnum: int):
        self.strings_list = [String(start_note, fretnum) for start_note in tuning]

    def update_tuning(self, new_tuning: list[Note]):
        self.tuning = new_tuning
        self.update_fretboard(self.tuning, self.fretnum)

    def update_fretnum(self, new_fretnum: int):
        self.fretnum = new_fretnum
        self.update_fretboard(self.tuning, self.fretnum)

    def find_note(self, a_note: AbstractNote) -> list[tuple[int, list[int]]]:
        all_notes = []

        for str_num, a_string in enumerate(self.strings_list):
            fret_nums = a_string.find_note(a_note)
            all_notes.append((str_num, fret_nums))
        return all_notes

    def find_notegroup(self, a_notegroup: NoteGroup):
        pass
