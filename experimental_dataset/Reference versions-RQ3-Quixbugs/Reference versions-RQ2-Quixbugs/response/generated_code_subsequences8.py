Program 1: Using Recursion
```
def subsequences(a, b, k):
    if k == 0:
        return [[]]
    ret = []
    for i in range(a, b+1-k+1):
        for seq in subsequences(i+1, b, k-1):
            ret.append([i] + seq)
    return ret
```

Program 2: Using Iteration

```
from itertools import combinations

def subsequences(a, b, k):
    ret = []
    for nums in combinations(range(a, b+1), k):
        if nums == tuple(sorted(nums)):
            ret.append(list(nums))
    return ret
```

Both programs function in the same way, producing all possible ascending subsequences of integers between a and b of length k. The first program uses recursion while the second program uses the comibation function from itertools module.