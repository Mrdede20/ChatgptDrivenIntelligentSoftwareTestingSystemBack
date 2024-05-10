
from collections import defaultdict

def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(len(items)):
        weight, value = items[i]
        for j in range(capacity + 1):
            if weight > j:
                memo[(i, j)] = memo[(i-1, j)]
            else:
                memo[(i, j)] = max(memo[(i-1, j)], memo[(i-1, j-weight)] + value)

    return memo[(len(items)-1, capacity)]
