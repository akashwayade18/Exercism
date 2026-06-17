def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    primes = [2]
    candidate = 3
    while len(primes) < number:
        is_prime = True
        upper_limit = candidate ** 0.5
        for p in primes:
            if p > upper_limit:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    return primes[-1]