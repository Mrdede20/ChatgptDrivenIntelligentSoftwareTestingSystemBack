
from itertools import permutations

def next_permutation(perm):
    for nxt in permutations(perm):
        if nxt > perm:
            return list(nxt)
