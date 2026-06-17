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

# using for loop
# def decode(string):
#     if len(string) == 0:
#         return ''
#     list_string = []
#     multiple = ''
#     for i in string:
#         if i.isdigit():
#             multiple += i
#         else:
#             if multiple == '':
#                 list_string.append((i, 1))
#             else:
#                 list_string.append((i, int(multiple)))
#             multiple = ''
#     return ''.join(inner[0] * inner[1] for inner in list_string)

# def encode(string):
#     if not string:
#         return ''
#     list_string = []
#     count = 1
#     for i in range(1, len(string)):
#         if string[i] == string[i - 1]:
#                 count += 1
#         else:
#             list_string.append((string[i - 1], str(count)))
#             count = 1
#     list_string.append((string[-1], str(count)))
#     return ''.join(inner[1]+inner[0] if int(inner[1]) > 1 else inner[0] for inner in list_string)


# USING REGEX
import re
def decode(string):
    if not string:
        return ""
        
    # Pattern explanation:
    # (\d*) optionally captures a multi-digit number into group 1
    # (\D) captures the mandatory non-digit character (letter/space) into group 2
    pattern = r'(\d*)(\D)'
    
    result = []
    for count, char in re.findall(pattern, string):
        # If group 1 was empty, count defaults to 1
        repeat = int(count) if count else 1
        result.append(char * repeat)
        
    return "".join(result)

def encode(string):
    if not string:
        return ''
    pattern = r'(.)\1*'
    result = []
    for match in re.finditer(pattern, string):
        group = match.group(0)  # The full streak, e.g., "WWWW"
        char = match.group(1)   # The specific character, e.g., "W"
        count = len(group)
        
        if count > 1:
            result.append(f"{count}{char}")
        else:
            result.append(char)
    return "".join(result)
