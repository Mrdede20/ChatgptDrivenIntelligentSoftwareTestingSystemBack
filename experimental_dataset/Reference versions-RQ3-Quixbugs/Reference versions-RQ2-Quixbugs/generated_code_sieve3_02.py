
def sieve(max):
    primes = list(range(2, max+1))
    for p in primes:
        if p:
            for n in range(p*p, max+1, p):
                primes[n-2] = None
    return [p for p in primes if p]
