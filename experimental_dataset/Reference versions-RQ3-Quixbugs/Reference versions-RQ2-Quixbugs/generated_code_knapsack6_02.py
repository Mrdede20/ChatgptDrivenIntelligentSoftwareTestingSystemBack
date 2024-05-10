
def knapsack_iterative_memoization(weights, values, capacity):
    memo = [[0] * (capacity + 1) for _ in range(len(weights))]
    
    for i in range(len(weights)):
        for j in range(capacity + 1):
            if j < weights[i]:
                memo[i][j] = memo[i - 1][j]
            else:
                include = values[i] + memo[i - 1][j - weights[i]]
                exclude = memo[i - 1][j]
                memo[i][j] = max(include, exclude)
    
    return memo[-1][-1]
