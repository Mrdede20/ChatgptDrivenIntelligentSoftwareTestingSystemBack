
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
