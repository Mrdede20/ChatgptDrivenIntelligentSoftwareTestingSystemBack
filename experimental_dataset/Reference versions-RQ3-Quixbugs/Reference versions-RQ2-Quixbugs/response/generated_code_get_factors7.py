Here are two programs implementing the `get_factors` function:

Program 1:
```python
def get_factors(n):
    if n == 1:
        return []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)
    return [n]
```

Program 2:
```python
def get_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1
    return factors if factors else []
```

Both programs implement the same logic to find the prime factors of an integer `n`. The first program uses recursion, while the second program uses a while loop. Both approaches have their pros and cons, and it's up to the developer to choose the implementation that suits their needs better.