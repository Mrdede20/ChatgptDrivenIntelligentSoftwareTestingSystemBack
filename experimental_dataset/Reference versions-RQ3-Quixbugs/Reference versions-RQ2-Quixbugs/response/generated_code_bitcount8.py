Program 1:

```python
def bitcount(n):
    count = 0 # Initialize count
    while (n):
        n &= (n-1) # clear the rightmost set bit
        count += 1
    return count
```

Program 2:

```python
def bitcount(n):
    count = 0 # Initialize count
    while (n != 0):
        n = (n & (n - 1)) # unset the rightmost set bit
        count += 1
    return count
```

Both of these programs implement the `bitcount` function using a while loop and the bitwise XOR operator `^`. They work by repeatedly subtracting 1 from `n` and performing a bitwise XOR operation between `n` and `n-1`. This clears the rightmost 1-bit in `n` until `n` becomes 0, and the number of iterations needed to achieve this is the number of 1-bits in the original binary encoding of `n`. The second program uses the `!=` operator instead of a truthy check to handle negative numbers. Both programs produce similar output and pass the provided test cases.