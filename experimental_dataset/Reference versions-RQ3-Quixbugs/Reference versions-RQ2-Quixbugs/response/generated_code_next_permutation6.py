Here's the first implementation using a function named "next_permutation":

```python
def next_permutation(perm):
    # Step 1
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    if i < 0:
        return None
    
    # Step 2
    j = len(perm) - 1
    while perm[j] <= perm[i]:
        j -= 1
    
    # Step 3
    perm[i], perm[j] = perm[j], perm[i]
    
    # Step 4
    perm[i + 1:] = reversed(perm[i + 1:])
    
    return perm
```

Here's the second implementation again using the same function name "next_permutation":

```python
def next_permutation(perm):
    # Step 1
    for i in reversed(range(len(perm) - 1)):
        if perm[i] < perm[i + 1]:
            break
    else:
        return None
    
    # Step 2
    for j in reversed(range(i + 1, len(perm))):
        if perm[j] > perm[i]:
            break
    
    # Step 3
    perm[i], perm[j] = perm[j], perm[i]
    
    # Step 4
    perm[i + 1:] = reversed(perm[i + 1:])
    
    return perm
```

Both these implementations use the same function name "next_permutation" and have the same parameter type, i.e., a list of unique integers. They have almost the same logic except for the way they find the indices i and j. The first implementation uses a while loop and the second one uses a for loop to iterate over the list.