
def knapsack(capacity, weights, values):
    n = len(values)
    memo = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                memo[i][j] = memo[i - 1][j]
    return memo[n][capacity]
