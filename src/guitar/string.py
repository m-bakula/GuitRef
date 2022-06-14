from src.notes.note import Note


class String:
    """Represents a single string tuned to a particular note"""
    def __init__(self, tuned_to: Note, frets: int) -> None:
        # TODO: put a constraint on strings containing notes out of bounds
        self.note_list = []
        for a_fret in range(frets+1):
            self.note_list.append(tuned_to.add_interval(a_fret))

    def get_note_at_fret(self, fret_num: int) -> Note:
        # fret_num can't be greater than self.frets:
        return self.note_list[fret_num]
