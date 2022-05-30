def fill_notes(names: list[str], octaves: list[int]) -> list[tuple[str, int]]:
    output = []
    for an_octave in octaves:
        output += [(a_name, an_octave) for a_name in names]
    return output


# list of all notes is created from lists of all note names and octaves
NOTE_NAMES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
NOTE_OCTAVES = [0, 1, 2, 3, 4, 5, 6, 7]
ALL_NOTES = fill_notes(NOTE_NAMES, NOTE_OCTAVES)


def indices_of(name: str) -> list[int]:
    output = []
    i = 0
    while i < len(ALL_NOTES):
        if ALL_NOTES[i][0] == name:
            output.append(i)
        i += 1
    return output


# dictionaries are created for interval names and positions of each note class in ALL_NOTES
INTERVALS_DICT = {0: 'root', 1: 'minor second', 2: 'major second', 3: 'minor third', 4: 'major third',
                  5: 'perfect fourth', 6: 'diminished fifth', 7: 'perfect fifth', 8: 'minor sixth', 9: 'major sixth',
                  10: 'minor seventh', 11: 'major seventh', 12: 'octave'}
POSITIONS_DICT = {name: indices_of(name) for name in NOTE_NAMES}
