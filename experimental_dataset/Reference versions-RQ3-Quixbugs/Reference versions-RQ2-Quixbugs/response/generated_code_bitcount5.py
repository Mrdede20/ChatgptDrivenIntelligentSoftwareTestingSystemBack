Sure, here are two programs that achieve the same intention:

Program 1:

```
def bitcount(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count
```

Program 2:

```
def bitcount(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
```

Both programs use the same method name and parameter type. The first program uses bit shifting and masking to count the number of 1-bits. The second program uses XOR and bitwise AND operations to count the number of 1-bits.