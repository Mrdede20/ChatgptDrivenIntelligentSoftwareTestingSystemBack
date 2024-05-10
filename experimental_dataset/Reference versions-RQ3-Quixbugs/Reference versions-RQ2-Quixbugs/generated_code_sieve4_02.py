
def sieve_of_eratosthenes(max):
    primes = []
    candidates = list(range(2, max + 1))
    while candidates:
        prime = candidates[0]
        primes.append(prime)
        candidates = [i for i in candidates if i % prime != 0]
    return primes
