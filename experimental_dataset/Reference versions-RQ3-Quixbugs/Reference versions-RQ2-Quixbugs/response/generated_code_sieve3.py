Sure, here are two implementations of the Sieve of Eratosthenes algorithm in Python:

Implementation 1:

```
def sieve(max):
    primes = []
    for n in range(2, max+1):
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes
```

Implementation 2:

```
def sieve(max):
    primes = list(range(2, max+1))
    for p in primes:
        if p:
            for n in range(p*p, max+1, p):
                primes[n-2] = None
    return [p for p in primes if p]
```

Both implementations take in a single parameter, `max`, representing the upper bound of the range of numbers to be checked for primality. The first implementation uses a nested loop to check if each number is divisible only by primes already in the `primes` list, while the second implementation uses list comprehension to remove multiples of each prime number from the `primes` list. Both implementations return a list of all the prime numbers up to and including `max`.