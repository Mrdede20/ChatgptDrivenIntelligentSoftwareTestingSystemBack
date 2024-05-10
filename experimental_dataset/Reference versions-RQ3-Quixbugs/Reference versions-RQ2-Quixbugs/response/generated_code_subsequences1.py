Here are two possible implementations for the same method name and parameter type:

1. Recursive approach:

```python
def generate_sequences(a, b, k):
    if k == 1:
        return [[i] for i in range(a, b+1)]
    
    result = []
    for i in range(a, b-k+2):
        sequences = generate_sequences(i+1, b, k-1)
        for sequence in sequences:
            result.append([i] + sequence)
    
    return result
```

2. Iterative approach:

```python
from itertools import combinations

def generate_sequences(a, b, k):
    result = []
    for comb in combinations(range(a, b+1), k):
        if list(comb) == sorted(comb):
            result.append(list(comb))
    
    return result
```

Both functions take three arguments: the lower bound `a`, the upper bound `b`, and the length of sequences `k`. The first implementation uses recursion to generate all possible sequences one element at a time, while the second implementation uses the `combinations` function from the `itertools` library to generate all possible combinations of length `k` from the range `[a, b]`, and then filters out those that are not sorted in ascending order. Both functions return a list of all generated sequences.