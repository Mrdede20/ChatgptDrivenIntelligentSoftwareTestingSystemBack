Here are the two solutions:

Program 1:
```python
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```

Program 2:
```python
def gcd(a: int, b: int) -> int:
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a
```

Both programs have the same method name and parameter type. They use the recursive and non-recursive approach to find the gcd of 'a' and 'b' by dividing 'a' by 'b' until the remainder is 0. The differences between these two implementations are in the manner of achieving this intention. While the first solution uses recursion to support the principle, the second one uses a loop.