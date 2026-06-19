import re

class PhoneNumber:
    def __init__(self, number):
        if any(c.isalpha() for c in number):
            raise ValueError("letters not permitted")

        allowed_symbols = set("0123456789 -.()+")
        if any(char not in allowed_symbols for char in number):
            raise ValueError("punctuations not permitted")

        cleaned = ''.join(c for c in number if c.isdigit())
        
        if len(cleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(cleaned) == 11:
            if cleaned[0] != '1':
                raise ValueError("11 digits must start with 1")
            cleaned = cleaned[1:]

        if cleaned[0] == '0':
            raise ValueError("area code cannot start with zero")
        elif cleaned[0] == '1':
            raise ValueError("area code cannot start with one")
        elif cleaned[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        elif cleaned[3] == '1':
            raise ValueError("exchange code cannot start with one")

        self.number = cleaned

    @property
    def area_code(self):
        return self.number[0:3]

    def pretty(self):
        return f'({self.number[0:3]})-{self.number[3:6]}-{self.number[6:10]}' 
        