
def knapsack(capacity, items):
    n = len(items)
    memo = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = items[i - 1]
        for j in range(1, capacity + 1):
            if w > j:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - w] + v)

    return memo[n][capacity]
