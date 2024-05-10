
from collections import defaultdict

def knapsack(capacity, items):
    memo = defaultdict(int)

    for weight, value in items:
        for i in range(capacity, weight - 1, -1):
            memo[i] = max(memo[i], memo[i - weight] + value)

    return memo[capacity]
