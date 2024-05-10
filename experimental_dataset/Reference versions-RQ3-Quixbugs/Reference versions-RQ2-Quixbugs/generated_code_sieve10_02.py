
def sieve_of_eratosthenes(max):
    primes = list(range(2, max+1))
    for i in range(len(primes)):
        if primes[i] == 0:
            continue
        for j in range(i+1, len(primes)):
            if primes[j] % primes[i] == 0:
                primes[j] = 0
    return [p for p in primes if p != 0]
