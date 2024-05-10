Program 1:

```python
def get_factors(n):
    factors = []
    if n == 1:
        return factors
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors
```

Program 2:

```python
def get_factors(n):
    factors = []
    if n == 1:
        return factors
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors
```

Both programs take integer `n` as input and return a list of prime factors of `n` in sorted order with repetition allowed. They use the trial division method to find the prime factors. Program 1 uses a `for` loop and Program 2 uses a `while` loop. Both programs check if `n` is divisible by the current integer and append it to the list of factors, update the value of `n`, and continue the loop until `n` becomes 1 or all factors are found.