
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
