Program 1:

```python
def sieve_of_eratosthenes(upper_bound):
    primes = []
    is_prime = [False, False] + [True] * (upper_bound - 1)
    
    for num in range(2, upper_bound + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, upper_bound + 1, num):
                is_prime[multiple] = False
    
    return primes
```

Program 2:

```python
def sieve_of_eratosthenes(upper_bound):
    primes = []
    is_prime = [True] * (upper_bound + 1)
    
    for num in range(2, upper_bound + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, upper_bound + 1, num):
                is_prime[multiple] = False
    
    return primes
```

Both of these programs implement the Sieve of Eratosthenes algorithm to generate a list of prime numbers up to a given upper bound. The first program uses a boolean list called `is_prime` to keep track of whether each number is prime or composite, while the second program initializes `is_prime` to just contain `True` values and assumes that every number is prime unless proven otherwise. However, both programs achieve the same result in terms of generating a list of primes.