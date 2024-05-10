Here are two implementations of the Sieve of Eratosthenes algorithm in Python:

Implementation 1:

```
def sieve_of_eratosthenes(max):
    primes = []
    is_prime = [True] * (max + 1)
    for num in range(2, max + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, max + 1, num):
                is_prime[multiple] = False
    return primes
```

In this implementation, we first create an empty list `primes` and a boolean list `is_prime` with `max+1` elements, all initialized to `True`. We then iterate through all the numbers from 2 to `max`. For each number, we check if it is marked as prime in `is_prime`. If it is, we add it to the `primes` list and mark all its multiples as non-prime in `is_prime`. Finally, we return the `primes` list.

Implementation 2:

```
def sieve_of_eratosthenes(max):
    primes = []
    candidates = list(range(2, max + 1))
    while candidates:
        prime = candidates[0]
        primes.append(prime)
        candidates = [i for i in candidates if i % prime != 0]
    return primes
```

In this implementation, we first create an empty list `primes` and a list `candidates` containing all numbers from 2 to `max`. We then enter a loop that runs as long as there are candidates left. Within the loop, we take the first element of `candidates` as the next prime number and add it to the `primes` list. We then remove all multiples of this prime number from `candidates`. Finally, we return the `primes` list.