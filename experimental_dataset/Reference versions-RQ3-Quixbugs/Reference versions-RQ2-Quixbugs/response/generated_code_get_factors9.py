Here are two programs that implement the `get_factors` function using the `naive trial division` algorithm with recursion:

Program 1:

```python
def get_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors
```

Program 2:

```python
def get_factors(n):
    def factor_helper(n, factor):
        if n == 1:
            return []
        elif n % factor == 0:
            return [factor] + factor_helper(n//factor, factor)
        else:
            return factor_helper(n, factor+1)
        
    return factor_helper(n, 2)
```

Both programs have the same method name `get_factors` and the same parameter type `n`, but they use slightly different implementations to achieve the same result. Program 1 uses a `while` loop to divide the input `n` by prime numbers until it is fully factored, while Program 2 uses a recursive helper function that checks the divisibility of `n` by prime numbers until it is fully factored. Program 2 also has an extra parameter `factor` that is used by the recursive helper function to keep track of the current prime factor being checked.