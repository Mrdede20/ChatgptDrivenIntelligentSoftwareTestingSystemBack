Here's one implementation of the `subsequences` function in Python using the described method:

``` python
def subsequences(a, b, k):
    if k == 0:
        return []
    ret = []
    for i in range(a, b + 1 - k):
        for seq in subsequences(i+1, b, k-1):
            ret.append([i] + seq)
    return ret
```

We can also write a more optimized version that uses list comprehension:

``` python
def subsequences(a, b, k):
    if k == 0:
        return []
    if k == 1:
        return [[i] for i in range(a, b+1)]
    return [[i]+seq for i in range(a, b+1-k+1) for seq in subsequences(i+1, b, k-1)]
```

This version avoids looping over the entire `range(a, b+1-k)` by returning the result directly when `k` is equal to 1. It also uses list comprehension instead of appending to a list in a for loop, which can be faster in some cases.