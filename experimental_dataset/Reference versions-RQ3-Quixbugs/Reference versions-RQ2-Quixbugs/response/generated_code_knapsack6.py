Here are two programs that solve the Knapsack problem using dynamic programming. The first program uses a recursive approach with memoization, while the second program uses an iterative approach with a memoization table.

Recursive approach with memoization:

```python
def knapsack_recursive_memoization(weights, values, capacity):
    memo = [[None] * (capacity + 1) for _ in range(len(weights))]
    
    def knapsack_helper(i, remaining_capacity):
        if i < 0 or remaining_capacity <= 0:
            return 0
        if memo[i][remaining_capacity] is not None:
            return memo[i][remaining_capacity]
        include = values[i] + knapsack_helper(i - 1, remaining_capacity - weights[i])
        exclude = knapsack_helper(i - 1, remaining_capacity)
        result = max(include, exclude)
        memo[i][remaining_capacity] = result
        return result
    
    return knapsack_helper(len(weights) - 1, capacity)
```

Iterative approach with memoization table:

```python
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
```