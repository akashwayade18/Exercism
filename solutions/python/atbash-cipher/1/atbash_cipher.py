# BRUTE FORCE
# CIPHER = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

# def encode(plain_text):
#     ciphered_text = ''
#     for char in plain_text.lower():
#         if char.isalpha():
#             ciphered_text += CIPHER[char]
#         if char.isdigit():
#             ciphered_text += char
#     return ' '.join([ciphered_text[i : i + 5] for i in range(0, len(ciphered_text), 5)])

# def decode(ciphered_text):
#     clean_ciphered_text = ciphered_text.replace(" ", "").lower()
#     clean_text = ''
#     for char in clean_ciphered_text:
#         if char.isalpha():
#             clean_text += CIPHER[char]
#         if char.isdigit():
#             clean_text += char
#     return clean_text

# OPTIMIZED APPROACH
import string
def encode(plain_text):
    encoded_text = translation(plain_text)
    return ' '.join([encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5)])

def decode(ciphered_text):
    return translation(ciphered_text)
    
def translation(text):
    plain_alphabet = string.ascii_lowercase
    ciphered_alphabet = plain_alphabet[::-1]
    atbash_directory = dict(zip(plain_alphabet, ciphered_alphabet))

    result = ''
    for char in text.lower():
        if char.isalnum():
            result += atbash_directory.get(char, char)
    return result
    
    
