# DICT does not work for repeating characters
# def decode(string):
#     result = ''
#     if len(string) == 0:
#         print('')
#     dict_encode = {}
#     multiple = ''
#     for i in string:
#         if i.isdigit():
#             if multiple == '':
#                 dict_encode[i] = 1
#             else:
#                 dict_encode[i] = int(multiple)
#             multiple = ''
#         else:
#             multiple += i
#     length = len(dict_encode)
#     for key, value in dict_encode.items():
#         result += key * int(value)
#     return result


def decode(string):
    if len(string) == 0:
        return ''
    list_string = []
    multiple = ''
    for i in string:
        if i.isdigit():
            multiple += i
        else:
            if multiple == '':
                list_string.append((i, 1))
            else:
                list_string.append((i, int(multiple)))
            multiple = ''
    return ''.join(inner[0] * inner[1] for inner in list_string)

def encode(string):
    if not string:
        return ''
    list_string = []
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
                count += 1
        else:
            list_string.append((string[i - 1], str(count)))
            count = 1
    list_string.append((string[-1], str(count)))
    return ''.join(inner[1]+inner[0] if int(inner[1]) > 1 else inner[0] for inner in list_string)
