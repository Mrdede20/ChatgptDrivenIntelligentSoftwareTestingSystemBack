
from collections import defaultdict

def knapsack(capacity, items):
    memo = defaultdict(int)

    for idx in range(len(items)):
        weight, value = items[idx]
        for cap in range(weight, capacity + 1):
            memo[cap] = max(memo[cap], memo[cap - weight] + value)

    return memo[capacity]
