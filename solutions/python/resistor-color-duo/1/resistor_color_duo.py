COLOR_CODES = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    ans = ""
    for color in colors[:2]:
        ans += str(COLOR_CODES.index(color))
    return int(ans)
