Program 1: 

```python
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
```

Program 2:

```python
def knapsack(capacity, items):
    n = len(items)
    memo = [0 for _ in range(capacity + 1)]

    for i in range(1, n + 1):
        w, v = items[i - 1]
        for j in range(capacity, w - 1, -1):
            memo[j] = max(memo[j], memo[j - w] + v)

    return memo[capacity]
```

Both programs implement a solution to the Knapsack Problem using dynamic programming. They differ in their implementation of memoization – program 1 uses a 2D list to store and reuse the results obtained in the subproblems of solving the original problem, while program 2 uses a 1D list. Both implementations have a time complexity of O(nc), where n is the number of items and c is the capacity of the knapsack. Program 2 is slightly more optimized since it uses less space.