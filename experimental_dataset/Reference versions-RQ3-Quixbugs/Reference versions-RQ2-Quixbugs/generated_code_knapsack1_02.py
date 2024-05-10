
from collections import defaultdict

def knapsack(capacity, items):
    dp = defaultdict(int)
    for item, value in items:
        for w in range(capacity+1):
            if item <= w:
                dp[w] = max(dp[w], dp[w-item] + value)
    return dp[capacity]
