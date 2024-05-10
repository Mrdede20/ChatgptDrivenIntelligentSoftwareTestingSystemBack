Sure, here are two programs that achieve this intention using dynamic programming to solve the Knapsack problem:

Program 1:
```
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
```

Program 2:
```
def knapsack(capacity, weights, values):
    n = len(values)
    memo = [0 for _ in range(capacity + 1)]
    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            memo[j] = max(memo[j], memo[j - weights[i]] + values[i])
    return memo[capacity]
```

Both programs take in the capacity of the knapsack, a list of weights for each item, and a list of corresponding values for each item. They both return the maximum value that can be obtained given the input.

Program 1 initializes a 2D array to store the maximum value that can be obtained for each combination of items and knapsack weight. It then iterates over each item and knapsack weight and updates the memoization table accordingly. Finally, it returns the maximum value that can be obtained given the input.

Program 2 initializes a 1D array to store the maximum value that can be obtained for each knapsack weight up to the given capacity. It then iterates over each item and updates the memoization table from the largest possible weight to the smallest possible weight. Finally, it returns the maximum value that can be obtained given the input.