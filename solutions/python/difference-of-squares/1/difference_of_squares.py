# BRUTE FORCE
# def square_of_sum(number):
#     sum = 1
#     for i in range (2, number+1):
#         sum += i
#     return sum ** 2

# def sum_of_squares(number):
#     squared_sum = 1
#     for i in range(2, number+1):
#         squared_sum += i ** 2
#     return squared_sum

# def difference_of_squares(number):
#     return square_of_sum(number) - sum_of_squares(number)

# OPTIMAL
def square_of_sum(number):
    return ((number * (number + 1)) // 2 ) ** 2

def sum_of_squares(number):
    return (number * (number + 1) * (2 * number + 1)) // 6

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
