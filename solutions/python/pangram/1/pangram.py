def is_pangram(sentence):
    compulsory = "abcdefghijklmnopqrstuvwxyz"
    for letter in compulsory:
        if letter not in sentence.lower():
            return False
    return True
