Sure, here are two versions of the implementation:

Version 1: Using recursion and backtracking:

```python
def generate_subsequences(a, b, k):
    if k == 0:
        return [[]]
    elif a > b:
        return []
    else:
        result = []
        for i in range(a, b+1):
            subsequences = generate_subsequences(i+1, b, k-1)
            for subseq in subsequences:
                result.append([i] + subseq)
        return result
```


Version 2: Using itertools:

```python
from itertools import combinations

def generate_subsequences(a, b, k):
    result = []
    for i in combinations(range(a, b+1), k):
        if list(i) == sorted(list(i)):
            result.append(list(i))
    return result
```

Both of these functions take in three arguments, 'a' and 'b' which define the range of the integers to consider (inclusive), and 'k' which is the length of the subsequences to generate. They both return a list of lists, each inner list containing a valid length-k ascending subsequence.