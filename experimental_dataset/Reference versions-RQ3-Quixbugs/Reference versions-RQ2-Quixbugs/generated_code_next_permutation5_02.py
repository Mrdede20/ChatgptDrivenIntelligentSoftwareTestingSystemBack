
import itertools

def next_permutation(perm):
    perms = itertools.permutations(perm)
    next_perm = None
    for p in perms:
        if p == perm:
            next_perm = next(perms, None)
            break
    return next_perm
