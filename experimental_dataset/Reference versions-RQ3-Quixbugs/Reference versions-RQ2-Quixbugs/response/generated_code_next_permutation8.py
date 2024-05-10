Sure, here are two programs for generating the lexicographically next permutation of a list of unique integers:

Program 1:

```python
def next_permutation(perm):
    # Find the largest index i such that perm[i] < perm[i+1]
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i+1]:
        i -= 1
    
    if i == -1:
        return None  # There is no next permutation
    
    # Find the largest index j such that perm[i] < perm[j]
    j = len(perm) - 1
    while perm[j] <= perm[i]:
        j -= 1
    
    # Swap the values at i and j
    perm[i], perm[j] = perm[j], perm[i]
    
    # Reverse the sublist from i+1 to the end of the list
    perm[i+1:] = reversed(perm[i+1:])
    
    return perm
```

Program 2:

```python
def next_permutation(perm):
    # Find the largest index i such that perm[i] < perm[i+1]
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i+1]:
        i -= 1
    
    if i == -1:
        return None  # There is no next permutation
    
    # Find the largest index j such that perm[i] < perm[j]
    j = len(perm) - 1
    while perm[j] <= perm[i]:
        j -= 1
    
    # Swap the values at i and j
    temp = perm[i]
    perm[i] = perm[j]
    perm[j] = temp
    
    # Reverse the sublist from i+1 to the end of the list
    temp_list = perm[i+1:]
    temp_list.reverse()
    perm[i+1:] = temp_list
    
    return perm
```

Both programs will take a list of unique integers as a parameter and return the lexicographically next permutation of that list, or `None` if there is no such permutation.