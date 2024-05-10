Sure, here are two programs:

First program:

```python
import math

def prime_factors(n):
    if n == 1:
        return []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return [i] + prime_factors(n // i)
    return [n]
```
Second program:

```python
def prime_factors(n):
    factors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors
```

Both programs have the same method name and parameter type, and implement a recursive function that takes an integer `n` and returns its prime factors as a list of integers. The first program uses recursion to call itself with the argument `n//i` and adds the factor `i` to the list that is returned. The second program uses a while loop to iterate over the range `2` to the square root of `n` (inclusive) checking if each number is a factor of `n` and adds it to the list of factors.