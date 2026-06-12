def rotate(text, key):
    new_text = ""
    for char in text:
        if char.isalpha():
            ord_no = ord(char) + key
            if char.islower():
                if ord_no > 122:
                    new_text += chr(96 + ord_no - 122)
                else:
                    new_text += chr(ord_no)
            else:
                if ord_no > 90:
                    new_text += chr(64 + ord_no - 90)
                else:
                    new_text += chr(ord_no)
        else:
            new_text += char
    return new_text