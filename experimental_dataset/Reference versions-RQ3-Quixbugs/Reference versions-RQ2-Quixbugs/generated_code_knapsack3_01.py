
from collections import defaultdict

def knapsack(weights, values, max_weight):
    memo = defaultdict(int)
    n = len(weights)
    
    for i in range(n):
        weight = weights[i]
        value = values[i]
        for capacity in range(max_weight, 0, -1):
            if weight <= capacity:
                memo[capacity] = max(memo[capacity], memo[capacity - weight] + value)
    
    return memo[max_weight]
