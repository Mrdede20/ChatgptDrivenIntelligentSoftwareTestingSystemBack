Here are two programs that implement the Euclidean algorithm to find the greatest common divisor of two non-negative integers 'a' and 'b', following the same method name and the same parameter type:

Program 1:

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

Program 2:

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

Both programs work following the same approach. The first program is implemented recursively, while the second program uses a while loop. The first program is generally preferred when there is a need to write a more compact code, and the second program is preferred when there is a need for better efficiency due to stack limitations.