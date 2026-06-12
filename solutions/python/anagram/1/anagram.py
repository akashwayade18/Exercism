def find_anagrams(word, candidates):
    anagrams = []
    # for inner_word in candidates:
    #     current = []
    #     for char in inner_word:
    #         if char.lower() in word.lower():
    #             current.append(char)
    #     if len(current) == len(word) and lower:
    #         anagrams.append(''.join(current))
    # return anagrams

    target_word_lower = word.lower()
    target_word_sorted = sorted(target_word_lower)

    for candidate in candidates:
        if sorted(candidate.lower()) == target_word_sorted and candidate.lower() != word.lower():
            anagrams.append(candidate)
    return anagrams