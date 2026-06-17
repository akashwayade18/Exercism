import re
from collections import Counter

def count_words(sentence):
    # doesn't cover all test cases
    # clean_sentence_list = re.sub(r'[^a-zA-Z0-9\s]', '', sentence).split(' ')
    # word_dict = {}
    # for i in clean_sentence_list:
    #     if i.isalnum():
    #         if word_dict.get(i):
    #             word_dict[i] += 1
    #         else:
    #             word_dict.setdefault(i, 1)
    # return word_dict

    lowercase_sentence = sentence.lower()
    
    # 2. Use regex to find all valid words.
    # [a-z0-9]+(?:'[a-z0-9]+)? matches alphanumeric words, 
    # and optionally matches an apostrophe followed by more alphanumeric characters (contractions).
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", lowercase_sentence)
    
    # 3. Use Counter to easily count the occurrences of each word
    word_dict = dict(Counter(words))
    
    return word_dict
