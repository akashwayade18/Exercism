scrabble_values = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

def score(word):
    # BRTUE FORCE
    # if not word:
    #     return 0
    # points = 0https://assets.exercism.org/assets/icons/run-tests-7259457020c0ad37ed70454416e07956cb5d40cf.svg
    # upper_word = word.upper()
    # for i in upper_word:
    #     points += scrabble_values[i]
    # return points

    # OPTIMAL APPROACH
    if not word:
        return 0
    upper_word = word.upper()
    return sum(scrabble_values.get(letter, 0) for letter in upper_word)