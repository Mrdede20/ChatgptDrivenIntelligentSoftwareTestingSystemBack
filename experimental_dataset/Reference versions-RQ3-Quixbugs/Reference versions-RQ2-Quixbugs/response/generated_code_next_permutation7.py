Here's the first Python program:

```python
def next_permutation(perm):
    n = len(perm)
    i = n - 2
    while i >= 0 and perm[i] >= perm[i+1]:
        i -= 1
    
    if i < 0:
        return None
    
    j = n - 1
    while perm[i] >= perm[j]:
        j -= 1
    
    perm[i], perm[j] = perm[j], perm[i]
    perm[i+1:] = reversed(perm[i+1:])
    return perm
```

Here's the second Python program, which optimizes step 2 using binary search:

```python
import bisect

def next_permutation(perm):
    n = len(perm)
    i = n - 2
    while i >= 0 and perm[i] >= perm[i+1]:
        i -= 1
    
    if i < 0:
        return None
    
    j = bisect.bisect_right(perm, perm[i], i+1)
    perm[i], perm[j] = perm[j], perm[i]
    perm[i+1:] = reversed(perm[i+1:])
    return perm
```

Both programs use the same method name and parameter type, and implement the same algorithm to find the lexicographically next permutation of a given list of unique integers. The second program optimizes step 2 by using binary search to find the smallest number to the right of the decreasing number that is still greater than it, instead of iterating through the rest of the list. This reduces the time complexity of the algorithm from O(n) to O(log n).