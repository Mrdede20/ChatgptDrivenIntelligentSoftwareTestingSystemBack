Program 1: 

```
def sieve(max):
    primes = []
    is_prime = [True] * (max+1)
    for num in range(2, max+1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num*num, max+1, num):
                is_prime[multiple] = False
    return primes
```

Program 2: 

```
def sieve(max):
    primes = []
    is_prime = [True] * (max+1)
    for num in range(2, max+1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num*num, max+1, num):
                is_prime[multiple] = False
    return primes
```

Both programs implement the Sieve of Eratosthenes algorithm to find all prime numbers in a range from 2 to a given positive integer `max`. They input `max` as a parameter and output a list of prime numbers up to and including `max`.