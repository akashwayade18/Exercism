CODES = ["wink", "double blink", "close your eyes", "jump"]
def commands(binary_str):
    final_code = []
    i = 1
    for char in binary_str[::-1]:
        if char == '1' and i == 1:
            final_code.append(CODES[0])
        elif char == '1' and i == 2:
            final_code.append(CODES[1])
        elif char == '1' and i == 3:
            final_code.append(CODES[2])
        elif char == '1' and i == 4:
            final_code.append(CODES[3])
        elif char == '1' and i == 5:
            final_code = final_code[::-1]
        i += 1
    return final_code
        
