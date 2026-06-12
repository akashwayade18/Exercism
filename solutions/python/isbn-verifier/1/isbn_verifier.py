def is_valid(isbn):
    clean_isbn = isbn.replace('-', '')
    if len(clean_isbn) != 10:
        return False
    if clean_isbn[-1].isalpha() and clean_isbn[-1].lower() != 'x':
        return False
    for char in clean_isbn[:len(clean_isbn)-1]:
        if char.isalpha():
            return False
    sum = 0
    constant = 10
    for char in clean_isbn:
        if char.upper() == 'X':
            char = 10
        sum += int(char) * constant
        constant -= 1
    return sum % 11 == 0
