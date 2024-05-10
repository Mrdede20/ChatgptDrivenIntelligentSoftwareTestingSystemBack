Here are two possible implementations of the Sieve of Eratosthenes algorithm:

Implementation 1:
```python
def sieve_of_eratosthenes(max):
    primes = []
    for num in range(2, max+1):
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
```

Implementation 2:
```python
def sieve_of_eratosthenes(max):
    primes = list(range(2, max+1))
    for i in range(len(primes)):
        if primes[i] == 0:
            continue
        for j in range(i+1, len(primes)):
            if primes[j] % primes[i] == 0:
                primes[j] = 0
    return [p for p in primes if p != 0]
```

Both of these implementations take in a positive integer `max` and use a list `primes` to store all the prime numbers found so far. The first implementation is an optimized version of the algorithm that checks each number for divisibility by all previously found primes. The second implementation is the traditional version of the algorithm that iteratively "crosses out" all numbers that are multiples of previously found primes using a list of integers.