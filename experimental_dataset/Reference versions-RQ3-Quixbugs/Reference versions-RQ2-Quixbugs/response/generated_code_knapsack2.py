Sure, here are two possible implementations:

Implementation 1:

```python
def knapsack(capacity, weights, values):
    n = len(weights)
    memo = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if j >= weights[i-1]:
                memo[i][j] = max(memo[i-1][j], values[i-1] + memo[i-1][j-weights[i-1]])
            else:
                memo[i][j] = memo[i-1][j]
    
    return memo[n][capacity]
```

Implementation 2:

```python
def knapsack(capacity, weights, values):
    n = len(weights)
    memo = [0 for _ in range(capacity+1)]
    
    for i in range(n):
        for j in range(capacity, weights[i]-1, -1):
            memo[j] = max(memo[j], memo[j-weights[i]] + values[i])
    
    return memo[capacity]
```

Both implementations use the dynamic programming approach to solve the knapsack problem. They take the capacity of the knapsack, a list of weights of the items, and a list of values of the items as input parameters. The first implementation uses a 2D memoization table to keep track of the maximum value of items that can be stored up to a given capacity, while the second implementation uses a 1D memoization table. In both cases, the function returns the maximum total value of the items that can be stored in the knapsack without exceeding its capacity.