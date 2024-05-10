Program 1:

```python
def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors
```

Program 2:

```python
def prime_factors(n, factor=2):
    if n == 1:
        return []
    if n % factor == 0:
        return [factor] + prime_factors(n//factor, factor)
    else:
        return prime_factors(n, factor+1)
```

Both programs take a single integer argument `n` and returns a list of prime factors of `n` in sorted order, including repetition if a prime factor appears more than once. 

The first program uses a while loop to successively divide `n` by all possible integer factors and appends each prime factor to the `factors` list. The second program uses recursion to divide `n` by smaller and smaller factors until it is completely factored.