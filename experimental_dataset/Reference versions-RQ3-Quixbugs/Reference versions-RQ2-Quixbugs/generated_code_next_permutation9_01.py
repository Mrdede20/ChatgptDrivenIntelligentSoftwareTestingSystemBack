
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
