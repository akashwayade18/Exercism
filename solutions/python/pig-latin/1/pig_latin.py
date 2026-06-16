# MY ATTEMPT
# def translate(text):
#     vowels = 'aeiou'
#     if (text.startswith('qu') or 'qu' in text) and text[:text.find('q')].lower() not in vowels:
#         return text[text.find('u')+1:] + text[:text.find('q')] + 'quay'
#     elif 'y' in text and text[:text.find('y')].lower() not in vowels:
#         return text[text.find('y'):] + text[:text.find('y')] + 'ay'
#     elif text.lower().startswith(('xr', 'yt', 'a', 'e', 'i', 'o','u')):
#         return text + 'ay'
#     else:
#         return text[text.find(('a', 'e', 'i', 'o', 'u')):] + text[:text.find(('a', 'e', 'i', 'o', 'u'))] + 'ay'

# OPTIMAL MY ATTEMPT
# def translate(text: str) -> str:
#     vowels = 'aeiou'
    
#     # Inner helper function to handle a single word
#     def translate_word(word: str) -> str:
#         # 1. Rule 1: Starts with vowel, 'xr', or 'yt'
#         if word.lower().startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
#             return word + 'ay'
            
#         # 2. Rule 3: Zero or more consonants followed by 'qu'
#         elif 'qu' in word:
#             pre_q = word[:word.find('q')].lower()
#             if all(char not in vowels for char in pre_q):
#                 u_index = word.find('u')
#                 return word[u_index + 1:] + word[:u_index + 1] + 'ay'
                
#         # 3. Rule 4: One or more consonants followed by 'y'
#         elif 'y' in word:
#             pre_y = word[:word.find('y')].lower()
#             if len(pre_y) > 0 and all(char not in vowels for char in pre_y):
#                 y_index = word.find('y')
#                 return word[y_index:] + word[:y_index] + 'ay'

#         # 4. Rule 2: Standard Consonants fallback
#         first_vowel_idx = next((i for i, char in enumerate(word.lower()) if char in vowels), 0)
#         return word[first_vowel_idx:] + word[:first_vowel_idx] + 'ay'

#     # Split the input sentence into words, process each, and join them back
#     return " ".join(translate_word(w) for w in text.split())

# REGEX VERSION
import re

def translate_word(word: str) -> str:
    # Rule 1: Starts with vowel, 'xr', or 'yt'
    if word.startswith(('a', 'e', 'i', 'o', 'u')) or word.startswith(('xr', 'yt')):
        return word + "ay"
        
    # Rule 3: Zero or more consonants followed by 'qu'
    # Match optional consonants at start (^[^aeiou]*) followed by 'qu'
    rule3_match = re.match(r"^([^aeiou]*qu)(.*)", word)
    if rule3_match:
        prefix, remainder = rule3_match.groups()
        return remainder + prefix + "ay"
        
    # Rule 4: One or more consonants followed by 'y'
    # Match 1+ consonants at start (^[^aeiou]+) followed by 'y'
    rule4_match = re.match(r"^([^aeiou]+)(y.*)", word)
    if rule4_match:
        prefix, remainder = rule4_match.groups()
        return remainder + prefix + "ay"
        
    # Rule 2: One or more consonants at the start
    # Match all leading consonants
    rule2_match = re.match(r"^([^aeiou]+)(.*)", word)
    if rule2_match:
        prefix, remainder = rule2_match.groups()
        return remainder + prefix + "ay"
        
    return word

def translate(text: str) -> str:
    """Translates a full sentence/phrase of words separated by spaces."""
    return " ".join(translate_word(word) for word in text.split())