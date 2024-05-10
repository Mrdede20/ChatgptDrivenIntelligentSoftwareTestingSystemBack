Program 1:

```
def subsequences(a, b, k):
    if k == 0:
        return [[]]
    if b-a+1 < k:
        return []
    ret = []
    for i in range(a, b+1-k+1):
        current = [[i] + seq for seq in subsequences(i+1, b, k-1)]
        ret.extend(current)
    return ret
```

Program 2:

```
def subsequences(a, b, k):
    if k == 0:
        return [[]]
    if b - a + 1 < k:
        return []
    result = []
    for i in range(a, b+1-k+1):
        for seq in subsequences(i+1, b, k-1):
            result.append([i] + seq)
    return result
```

Both programs use the same method name `subsequences` and parameter types of `a` (starting integer), `b` (maximum integer), and `k` (length of subsequences to generate). The programs recursively generate subsequences of the given length `k` within the range `[a, b]` and return a list containing all generated subsequences.