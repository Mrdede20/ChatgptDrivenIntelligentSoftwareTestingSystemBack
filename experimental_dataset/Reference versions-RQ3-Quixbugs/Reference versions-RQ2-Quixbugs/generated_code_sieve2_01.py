
def sieve_of_eratosthenes(max):
    primes = []
    for n in range(2, max+1):
        if all(n % p > 0 for p in primes):
            primes.append(n)
    return primes
