
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
