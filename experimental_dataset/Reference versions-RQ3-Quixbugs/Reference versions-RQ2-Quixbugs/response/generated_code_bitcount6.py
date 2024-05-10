Here are two Python programs that achieve this intention:

Program 1:

```python
def bitcount(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

# test cases
assert bitcount(0) == 0
assert bitcount(1) == 1
assert bitcount(2) == 1
assert bitcount(7) == 3
assert bitcount(256) == 1
```

Program 2:

```python
def bitcount(n):
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count

# test cases
assert bitcount(0) == 0
assert bitcount(1) == 1
assert bitcount(2) == 1
assert bitcount(7) == 3
assert bitcount(256) == 1
```

Both programs define the `bitcount` function that takes a non-negative integer `n` as input and returns the number of 1-bits in the binary encoding of `n`. The implementation uses an efficient algorithm that iteratively flips the rightmost set bit of `n` while counting the number of iterations until `n` becomes 0.

The test cases ensure the correctness of the implementation by checking the output against expected results for several inputs.