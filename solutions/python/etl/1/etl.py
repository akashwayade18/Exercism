def transform(legacy_data):
    # little slow due to setdefault as it checks first if the key exist or not
    # new_data = {}
    # for key in legacy_data.keys():
    #     iterable = legacy_data[key]
    #     for item in iterable:
    #         new_data.setdefault(item.lower(), key)

    # more optimised version for direct assignment
    # new_data = {}
    # for score, letters in legacy_data.items():
    #     for letter in letters:
    #         new_data[letter.lower()] = score
    # return new_data

    # DICT COMPREHENSION
    return {letter.lower() : score for score, letters in legacy_data.items() for letter in letters}