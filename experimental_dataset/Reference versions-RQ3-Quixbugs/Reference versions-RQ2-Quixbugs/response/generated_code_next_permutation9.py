Here are two Python programs that solve the "Next Permutation" problem. Both programs use the same method name `next_permutation` and have the same parameter type `List[int]`.

Program 1:

```python
def next_permutation(perm: List[int]) -> Optional[List[int]]:
    # Find the rightmost pair of adjacent elements in increasing order
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    
    # If no such pair is found, the elements are in decreasing order
    if i < 0:
        return None
    
    # Find the smallest element to the right of the pivot that is greater than it
    j = len(perm) - 1
    while perm[j] <= perm[i]:
        j -= 1
    
    # Swap the pivot with the smallest element to its right that is greater than it
    perm[i], perm[j] = perm[j], perm[i]
    
    # Reverse the elements to the right of the pivot
    perm[i + 1:] = reversed(perm[i + 1:])
    
    return perm
```

Program 2:

```python
def next_permutation(perm: List[int]) -> Optional[List[int]]:
    # Find the pivot position - the index of the last element in a non-increasing suffix
    pivot = len(perm) - 2
    while pivot >= 0 and perm[pivot] >= perm[pivot + 1]:
        pivot -= 1
    
    # If no pivot is found, the sequence is already the last permutation
    if pivot < 0:
        return None
    
    # Find the rightmost element greater than the pivot and swap them
    successor = len(perm) - 1
    while perm[successor] <= perm[pivot]:
        successor -= 1
    perm[pivot], perm[successor] = perm[successor], perm[pivot]
    
    # Reverse the suffix
    perm[pivot + 1:] = perm[-1:pivot:-1]
    
    return perm
```