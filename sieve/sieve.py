def primes(limit, primes=[2]):
    for i in range(3, limit + 1, 2):
        if all(i % prime != 0 for prime in primes):
            primes += [i]
    return primes if limit > 1 else []
