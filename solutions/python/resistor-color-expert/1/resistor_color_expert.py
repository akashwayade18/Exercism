COLOR_CODES = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
TOLERANCE = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver":10}

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    if len(colors) == 4:
        bands = int(str(COLOR_CODES.index(colors[0])) + str(COLOR_CODES.index(colors[1])))
        multiplier = COLOR_CODES.index(colors[2])
        tolerance = TOLERANCE[colors[3]]

    if len(colors) == 5:
        bands = int(str(COLOR_CODES.index(colors[0])) + str(COLOR_CODES.index(colors[1])) + str(COLOR_CODES.index(colors[2])))
        multiplier = COLOR_CODES.index(colors[3])
        tolerance = TOLERANCE[colors[4]]
        
    raw_ohms = bands * (10 ** multiplier)
    if raw_ohms >= 1000000000:
        value = raw_ohms / 1000000000
        suffix = "gigaohms"
    elif raw_ohms >= 1000000:
        value = raw_ohms / 1000000
        suffix = "megaohms" 
    elif raw_ohms >= 1000:
        value = raw_ohms / 1000
        suffix = "kiloohms"
    else:
        value = raw_ohms
        suffix = "ohms"
    if value == int(value):
        value = int(value)
    return f"{value} {suffix} \u00b1{tolerance}%"