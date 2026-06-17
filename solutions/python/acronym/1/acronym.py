import re
def abbreviate(words):
    # BRUTE FORCE
    # words_clean = words.replace('-',' ')
    # words_list = words_clean.split(' ')
    # acronym = ''
    # for word in words_list:
    #     for i in word:
    #         if i.isalpha():
    #             acronym += i.upper()
    #             break
    # return acronym

    # OPTIMAL APPROACH
    clean_words = words.replace('-', ' ')
    clean_words = clean_words.replace('_', ' ')
    cleaner_words = re.sub(r'[^a-zA-Z\s]', '', clean_words)
    words_list = clean_words.split()
    acronym = [word[0].upper() for word in words_list]
    return ''.join(acronym)
