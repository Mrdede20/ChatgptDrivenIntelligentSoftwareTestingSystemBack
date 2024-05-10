
from collections import defaultdict

def knapsack(capacity, items):
    n = len(items)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        w, v = items[i-1]
        for j in range(1, capacity+1):
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    return dp[-1][-1]
