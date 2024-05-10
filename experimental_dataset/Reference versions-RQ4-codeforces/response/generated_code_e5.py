Solution 1:

```
def BinaryInversions(n, bits):
    first = 0
    second = 0
    for i in range(n-1):
        if bits[i] == 0 and bits[i+1] == 1:
            first += 1
    for i in range(n-2):
        if bits[i] == 0 and bits[i+1] == 1 and bits[i+2] == 0:
            second += 1
            bits[i:i+3] = [1,0,1]
    max_inversions = first + second*2
    return max_inversions
```

Solution 2:

```
def BinaryInversions(n, bits):
    first = 0
    second = 0
    for i in range(n-1):
        if bits[i] == 0 and bits[i+1] == 1:
            first += 1
    for i in range(n-2):
        if bits[i] == 0 and bits[i+1] == 1 and bits[i+2] == 0:
            second += 1
            bits[i] = 1
            bits[i+1] = 0
            bits[i+2] = 1
    max_inversions = first + second*2
    return max_inversions
```

Both solutions achieve the same purpose, where we first check for first and second inversions and replace them with an inverted equivalent when possible, then calculate and return the maximum number of inversions. However, the difference between the two solutions is in how the replacements are made. Solution 1 replaces the inverted equivalent as a sublist, while Solution 2 replaces each bit separately.