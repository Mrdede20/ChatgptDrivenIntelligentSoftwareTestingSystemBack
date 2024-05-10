Sure, here are two implementations:

Implementation 1:

```python
def next_permutation(perm):
    # Find the largest index k such that perm[k] < perm[k + 1]
    k = len(perm) - 2
    while k >= 0 and perm[k] >= perm[k+1]:
        k -= 1
    if k == -1: # List is already the largest possible permutation
        return None
    
    # Find the largest index l greater than k such that perm[k] < perm[l]
    l = len(perm) - 1
    while l > k and perm[k] >= perm[l]:
        l -= 1
    
    # Swap perm[k] and perm[l]
    perm[k], perm[l] = perm[l], perm[k]
    
    # Reverse the sequence from perm[k+1] up to and including the final element of the list
    perm[k+1:] = perm[:k:-1]
    return perm
```

Implementation 2:

```python
def next_permutation(perm):
    # Find the largest index k such that perm[k] < perm[k + 1]
    k = -1
    for i in range(len(perm)-1):
        if perm[i] < perm[i+1]:
            k = i
    
    if k == -1: # List is already the largest possible permutation
        return None
    
    # Find the largest index l greater than k such that perm[k] < perm[l]
    l = len(perm) - 1
    while perm[k] >= perm[l]:
        l -= 1
    
    # Swap perm[k] and perm[l]
    perm[k], perm[l] = perm[l], perm[k]
    
    # Reverse the sequence from perm[k+1] up to and including the final element of the list
    perm[k+1:] = perm[:k:-1]
    return perm
```

Both implement the same algorithm with the same time and space complexity, but use slightly different logic to find the indices k and l.