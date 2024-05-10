
def knapsack(capacity, items):
    memo = {}
    for i in range(1, capacity + 1):
        memo[i] = 0
    for item_weight, item_value in items:
        for i in range(capacity, 0, -1):
            if item_weight <= i:
                memo[i] = max(memo[i], memo[i - item_weight] + item_value)
    return memo[capacity]
