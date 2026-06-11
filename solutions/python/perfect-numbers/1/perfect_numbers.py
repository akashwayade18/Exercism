def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    sum_factors = sum(a for a in range(1, number) if number % a == 0)
    if sum_factors == number:
        return "perfect"
    elif sum_factors < number:
        return "deficient"
    else:
        return "abundant"
    
