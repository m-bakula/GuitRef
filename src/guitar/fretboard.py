from src.notes.note import AbstractNote, Note
from src.guitar.string import String


class Fretboard:
    """Represents a fretboard with strings tuned to given notes and a given number of frets"""
    def __init__(self, frets: int, tuning: list[Note]) -> None:
        self.frets: int = frets
        self.strings_list: list[String] = [String(start_note, frets) for start_note in tuning]

    def find_note(self, a_note: AbstractNote) -> list:
        pass
