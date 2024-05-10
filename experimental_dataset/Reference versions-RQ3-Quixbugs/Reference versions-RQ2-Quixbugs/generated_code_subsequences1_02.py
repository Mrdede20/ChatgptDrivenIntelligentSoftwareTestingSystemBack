
from itertools import combinations

def generate_sequences(a, b, k):
    result = []
    for comb in combinations(range(a, b+1), k):
        if list(comb) == sorted(comb):
            result.append(list(comb))
    
    return result
