Here are two possible implementations of the `bitcount` function using the method described in the prompt:

Implementation 1:
```python
def bitcount(n):
    # handle negative input values
    if n < 0:
        n = 2 ** 32 + n # compute 2's complement representation
        
    count = 0
    while n != 0:
        n ^= n & -n # toggle least significant 1-bit
        count += 1
        
    return count
```

Implementation 2:
```python
def bitcount(n):
    # handle negative input values
    if n < 0:
        n = 2 ** 32 + n # compute 2's complement representation
        
    count = 0
    while n:
        count += 1
        n &= n - 1 # clear least significant 1-bit
        
    return count
```

Both implementations use bitwise operations to efficiently count the number of 1-bits in the binary representation of `n`. The second implementation uses a well-known optimization trick that clears the least significant 1-bit in `n` using `n &= n - 1` instead of toggling it with a bitwise XOR operation. The choice between the two implementations mostly boils down to personal preference and coding style.