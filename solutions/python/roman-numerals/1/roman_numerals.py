def roman(number):
    ROMAN_MAP = (
        (1000, 'M'),  (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'),   (90, 'XC'),  (50, 'L'),  (40, 'XL'),
        (10, 'X'),    (9, 'IX'),   (5, 'V'),   (4, 'IV'),
        (1, 'I')
    )
    
    result = []
    
    for value, symbol in ROMAN_MAP:
        if number == 0:
            break
            
        # Optimization: Determine how many times the symbol fits using floor division
        count = number // value
        if count > 0:
            result.append(symbol * count)
            number %= value  # Keep the remainder for the next iteration
            
    return "".join(result)