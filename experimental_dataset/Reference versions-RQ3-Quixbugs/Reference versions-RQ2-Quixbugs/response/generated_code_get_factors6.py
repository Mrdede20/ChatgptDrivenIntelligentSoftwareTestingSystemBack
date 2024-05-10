Program 1:

```python
def get_factors(n):
    factors = []
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            factors.append(i)
            n //= i
            factors.extend(get_factors(n))
            return factors
    factors.append(n)
    return factors
```

Program 2:

```python
def get_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
```

Both programs have the same function name and parameter type. The programs use similar logic to compute the prime factorization of a positive integer `n`. The first program is implemented using recursion, while the second program uses a while loop to compute the prime factorization.