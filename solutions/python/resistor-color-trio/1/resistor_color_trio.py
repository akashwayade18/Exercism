COLOR_CODES = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

def label(colors):
    band1 = COLOR_CODES.index(colors[0])
    band2 = COLOR_CODES.index(colors[1])
    multiplier = COLOR_CODES.index(colors[2])

    raw_ohms = (band1 * 10 + band2) * (10 ** multiplier)

    if raw_ohms >= 1000000000:
        value = raw_ohms // 1000000000
        suffix = "gigaohms"
    elif raw_ohms >= 1000000:
        value = raw_ohms // 1000000
        suffix = "megaohms"
    elif raw_ohms >= 1000:
        value = raw_ohms // 1000
        suffix = "kiloohms"
    else:
        value = raw_ohms
        suffix = "ohms"

    return f"{value} {suffix}"
    # cannot cover all edge cases
    # resistance = str(COLOR_CODES.index(colors[0])) + str(COLOR_CODES.index(colors[1])) + str('0' * COLOR_CODES.index(colors[2]))
    # count = 0
    # for i in resistance[::-1]:
    #     if i == str(0):
    #         count += 1
    #     else:
    #         break
    # ohms_prefix = "ohms"
    # if 3 <= count < 6:
    #     ohms_prefix = "kiloohms"
    # if 6 <= count < 9:
    #     ohms_prefix = "megaohms"
    # if 9 <= count < 12:
    #     ohms_prefix = "gigaohms"
        
    # end_no = len(resistance) - count + 1 if count % 2 == 0 else len(resistance) - count
    # return (resistance[: end_no] + " " + ohms_prefix)