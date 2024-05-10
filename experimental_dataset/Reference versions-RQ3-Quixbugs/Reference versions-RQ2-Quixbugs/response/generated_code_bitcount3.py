Program 1:

```
def bitcount(n):
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1
    return count
```

Program 2:

```
def bitcount(n):
    count = 0
    while n:
        count += 1
        n = n & (n - 1)
    return count
```

Both programs achieve the same objective of counting the number of 1-bits in the binary representation of a non-negative integer `n`. The first program uses a while loop to keep shifting bits to the right and adding the least significant bit to a count variable until the input number becomes zero. The second program uses a while loop to repeatedly clear the least significant 1-bit and increment a count variable until the input number becomes zero. Both algorithms are efficient in terms of time complexity, with the second program being slightly faster than the first.