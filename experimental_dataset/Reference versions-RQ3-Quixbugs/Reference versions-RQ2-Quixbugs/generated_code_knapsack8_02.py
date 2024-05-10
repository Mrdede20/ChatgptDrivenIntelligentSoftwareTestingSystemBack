
def knapsack(capacity, items):
    n = len(items)
    memo = [0 for _ in range(capacity + 1)]

    for i in range(1, n + 1):
        w, v = items[i - 1]
        for j in range(capacity, w - 1, -1):
            memo[j] = max(memo[j], memo[j - w] + v)

    return memo[capacity]
