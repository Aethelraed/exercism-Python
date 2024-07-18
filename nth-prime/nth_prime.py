def next_prime(primes):
    prim = primes[-1]
    while any(prim %p==0 for p in primes): prim +=2
    return prim
def prime(number,primes = [2,3]):
    if number <1:raise ValueError("there is no zeroth prime")    
    while len(primes)<number: primes.append(next_prime(primes))
    return primes[-1] if number > len(primes)-1 else primes[number-1]
        


