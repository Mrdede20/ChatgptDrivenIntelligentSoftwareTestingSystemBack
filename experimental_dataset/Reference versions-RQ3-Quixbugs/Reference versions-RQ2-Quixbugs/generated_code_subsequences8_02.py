
from itertools import combinations

def subsequences(a, b, k):
    ret = []
    for nums in combinations(range(a, b+1), k):
        if nums == tuple(sorted(nums)):
            ret.append(list(nums))
    return ret
