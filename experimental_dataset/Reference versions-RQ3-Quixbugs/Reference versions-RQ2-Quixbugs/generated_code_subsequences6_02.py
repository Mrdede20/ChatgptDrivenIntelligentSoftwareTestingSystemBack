
from itertools import combinations

def generate_subsequences(a, b, k):
    result = []
    for i in combinations(range(a, b+1), k):
        if list(i) == sorted(list(i)):
            result.append(list(i))
    return result
