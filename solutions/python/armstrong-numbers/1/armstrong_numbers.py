def is_armstrong_number(number):
    # sum = 0
    # temp = 0
    # power = len(str(number))
    # num = number
    # while(number>0):
    #     temp = number % 10
    #     sum += temp ** power
    #     number //= 10
    # return sum == num

    ''' more optimized approach'''
    power = len(str(number))
    return sum(int(digit) ** power for digit in str(number)) == number