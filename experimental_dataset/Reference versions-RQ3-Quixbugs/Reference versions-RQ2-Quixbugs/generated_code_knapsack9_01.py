
from collections import defaultdict

def knapsack(capacity, items):
    dp = defaultdict(int)
    for w, v in items:
        for i in range(capacity, w-1, -1):
            dp[i] = max(dp[i], dp[i-w] + v)
    return dp[capacity]
