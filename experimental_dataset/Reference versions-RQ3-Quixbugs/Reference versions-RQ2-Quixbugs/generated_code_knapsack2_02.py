
def knapsack(capacity, weights, values):
    n = len(weights)
    memo = [0 for _ in range(capacity+1)]
    
    for i in range(n):
        for j in range(capacity, weights[i]-1, -1):
            memo[j] = max(memo[j], memo[j-weights[i]] + values[i])
    
    return memo[capacity]
