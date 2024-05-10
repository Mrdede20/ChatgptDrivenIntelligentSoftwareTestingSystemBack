
from collections import defaultdict

def knapsack(weights, values, max_weight):
    memo = defaultdict(int)
    n = len(weights)
    
    for i in range(1, n+1):
        weight = weights[i-1]
        value = values[i-1]
        for capacity in range(1, max_weight+1):
            if weight <= capacity:
                memo[(i, capacity)] = max(memo[(i-1, capacity)], memo[(i-1, capacity-weight)] + value)
            else:
                memo[(i, capacity)] = memo[(i-1, capacity)]
    
    return memo[(n, max_weight)]
