Here are two programs that implement the Sieve of Eratosthenes algorithm for finding all the prime numbers up to a given number `max`:

Program 1:

```python
def sieve_of_eratosthenes(max):
    primes = []
    for n in range(2, max+1):
        if all(n % p > 0 for p in primes):
            primes.append(n)
    return primes
```

Program 2:

```python
def sieve_of_eratosthenes(max):
    primes = []
    for n in range(2, max+1):
        if not any(n % p == 0 for p in primes):
            primes.append(n)
    return primes
```

Both programs take an integer `max` as input and return a list of primes up to and including `max`. The first program uses the `all` function and the second program uses the `any` function, but the logic is essentially the same: for each number `n`, check if it is divisible by any of the primes found so far. If not, then `n` is a prime and is added to the list of primes. Both programs should have the same output for the same input `max`.