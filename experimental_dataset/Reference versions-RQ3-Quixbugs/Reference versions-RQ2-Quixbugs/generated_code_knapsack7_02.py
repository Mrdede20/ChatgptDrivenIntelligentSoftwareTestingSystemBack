
def knapsack(capacity, items):
    memo = {}
    for i in range(1, capacity + 1):
        memo[i] = 0
    for item in items:
        for i in range(capacity, item[0] - 1, -1):
            memo[i] = max(memo[i], memo[i - item[0]] + item[1])
    return memo[capacity]
