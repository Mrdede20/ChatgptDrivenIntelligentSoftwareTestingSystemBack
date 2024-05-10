Here are the two programs to calculate the greatest common divisor (GCD) of two non-negative integers `a` and `b` using the Euclidean algorithm:

Program 1:

```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```

Program 2:

```python
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a
```

Both the programs use the same method name `gcd()` and take the same parameter type i.e. two non-negative integers `a` and `b`. Program 1 uses recursion to calculate the GCD while Program 2 uses a while loop to achieve the same result. Program 2 is more efficient as it avoids the overhead of recursive function calls.