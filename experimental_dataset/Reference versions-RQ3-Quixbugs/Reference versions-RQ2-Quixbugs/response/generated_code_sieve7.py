Program 1:

```
def sieve_of_eratosthenes(max):
    primes = []
    for n in range(2, max+1):
        if not any(n % p == 0 for p in primes):
            primes.append(n)
    return primes
```

Program 2 (optimized):

```
def sieve_of_eratosthenes(max):
    primes = [True] * (max+1)
    primes[0] = primes[1] = False
    for n in range(2, int(max**0.5)+1):
        if primes[n]:
            for i in range(n**2, max+1, n):
                primes[i] = False
    return [n for n, is_prime in enumerate(primes) if is_prime]
```

Both programs implement the Sieve of Eratosthenes algorithm to generate all the prime numbers up to and including a given upper bound. The first program uses a list of previously found primes to check if a number is prime, while the second program uses a boolean list to mark off multiples of prime numbers as composite. The second program is more optimized as it only checks up to the square root of the upper bound and skips multiples of non-prime numbers, resulting in a faster implementation.