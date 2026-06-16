def line_up(name, number):
    # BRUTE FORCE SOLUTION
    # suffix_number = ""
    # number_str = str(number)
    # if number_str.endswith('1') and (not number_str.endswith('11')):
    #     suffix_number = number_str + 'st'
    # elif number_str.endswith('2') and (not number_str.endswith('12')):
    #     suffix_number = number_str + 'nd'
    # elif number_str.endswith('3') and (not number_str.endswith('13')):
    #     suffix_number = number_str + 'rd'
    # else:
    #     suffix_number = number_str + 'th'
    # return f"{name}, you are the {suffix_number} customer we serve today. Thank you!"

    # OPTIMAL APPROACH
    # if 11 <= number % 100 <= 13:
    #     suffix = 'th'
    # else:
    #     suffix = {1: 'st', 2: 'nd', 3:'rd'}.get(number % 10, 'th')
    # return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"

    # ONE - LINER APPROACH
    suffix = 'th' if 11 <= number % 100 <= 13 else ['th', 'st', 'nd', 'rd'][number % 10] if number % 10 < 4 else 'th'
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
