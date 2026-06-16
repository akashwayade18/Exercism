def rows(letter):
    # APPROACH 1
    # length = ord(letter) - 64
    # result = []
    # for i in range(1, length+1):
    #     leading_spaces = ' ' * (length - i)
    #     current_char = chr(i+64)
    #     if i == 1:
    #         result += [leading_spaces + current_char + leading_spaces]
    #     else:
    #         internal_spaces = ' '* (2 * i - 3)
    #         result += [leading_spaces + current_char + internal_spaces + current_char + leading_spaces]
    
    
    # for i in range(length - 1, 0, -1):
    #     leading_spaces = ' ' * (length - i)
    #     current_char = chr(i+64)
    #     if i == 1:
    #         result += [leading_spaces + current_char + leading_spaces]
    #     else:
    #         internal_spaces = ' '* (2 * i - 3)
    #         result += [leading_spaces + current_char + internal_spaces + current_char + leading_spaces]
    # return result

    # APPROACH 2
    letters = [chr(k) for k in range(ord('A'), ord(letter) + 1)]
    alphabet = letters[:-1] + letters[::-1]
    diamond_line = letters[::-1] + letters[1:]
    return [''.join(x if x == y else ' ' for y in diamond_line) for x in alphabet]