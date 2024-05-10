Here are the two programs that achieves this intention - 

Program 1:

```python
def bitcount(n):
    count = 0
    while n != 0:
        n &= n - 1
        count += 1
    return count
```

Program 2:

```python
def bitcount(n):
    if n < 0:
        return 0
    count = 0
    while n != 0:
        n ^= n - 1
        count += 1
    return count
```

Both of the programs implements the `bitcount` function that takes a non-negative integer `n` and returns the number of 1-bits in the binary encoding of `n`. The first program is an optimized version of the code given in the problem, while the second program handles negative numbers by returning 0 when `n` is negative.