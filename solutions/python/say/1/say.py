def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    if number == 0:
        return 'zero'
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands_groups = ["", "thousand", "million", "billion"]
    def helper(n):
        words = []
        
        # Handle hundreds place
        if n >= 100:
            words.append(ones[n // 100] + " hundred")
            n %= 100
            
        # Handle tens and ones place
        if 10 <= n < 20:
            words.append(teens[n - 10])
        elif n >= 20:
            tens_place = tens[n // 10]
            ones_place = ones[n % 10]
            # Include a hyphen for numbers like twenty-three
            if ones_place:
                words.append(f"{tens_place}-{ones_place}")
            else:
                words.append(tens_place)
        elif n > 0:
            words.append(ones[n])
            
        return " ".join(words)

    # 2. Main logic to break the number into chunks of thousands
    result_chunks = []
    group_idx = 0

    while number > 0:
        chunk = number % 1000
        if chunk > 0:
            chunk_words = helper(chunk)
            # Append the scale (thousand, million, billion) if applicable
            if thousands_groups[group_idx]:
                chunk_words += f" {thousands_groups[group_idx]}"
            result_chunks.append(chunk_words)
            
        number //= 1000
        group_idx += 1

    # Reverse the chunks so they read from largest to smallest (billion -> million -> etc.)
    return " ".join(reversed(result_chunks))