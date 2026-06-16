def rows(letter):
    length = ord(letter) - 64
    result = []
    for i in range(1, length+1):
        leading_spaces = ' ' * (length - i)
        current_char = chr(i+64)
        if i == 1:
            result += [leading_spaces + current_char + leading_spaces]
        else:
            internal_spaces = ' '* (2 * i - 3)
            result += [leading_spaces + current_char + internal_spaces + current_char + leading_spaces]
    
    
    for i in range(length - 1, 0, -1):
        leading_spaces = ' ' * (length - i)
        current_char = chr(i+64)
        if i == 1:
            result += [leading_spaces + current_char + leading_spaces]
        else:
            internal_spaces = ' '* (2 * i - 3)
            result += [leading_spaces + current_char + internal_spaces + current_char + leading_spaces]
    return result