
def sieve_of_eratosthenes(max):
    primes = [True] * (max+1)
    primes[0] = primes[1] = False
    for n in range(2, int(max**0.5)+1):
        if primes[n]:
            for i in range(n**2, max+1, n):
                primes[i] = False
    return [n for n, is_prime in enumerate(primes) if is_prime]
