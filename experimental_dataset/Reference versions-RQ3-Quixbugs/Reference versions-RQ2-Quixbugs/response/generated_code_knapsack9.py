Program 1:

```python
from collections import defaultdict

def knapsack(capacity, items):
    dp = defaultdict(int)
    for w, v in items:
        for i in range(capacity, w-1, -1):
            dp[i] = max(dp[i], dp[i-w] + v)
    return dp[capacity]
```

Program 2:

```python
from collections import defaultdict

def knapsack(capacity, items):
    n = len(items)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        w, v = items[i-1]
        for j in range(1, capacity+1):
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    return dp[-1][-1]
```

Both programs implement dynamic programming to solve the Knapsack problem using the same function name and parameter types. Program 1 uses a defaultdict to store the maximum total value that can be obtained given a specific weight threshold and a subset of the items list. It iterates through the items and capacity to find the maximum value that can be obtained given the current item and the capacity of the knapsack. Program 2 uses a 2D list to achieve the same result. Both programs have a time complexity of O(nc) where n is the number of items in the list and c is the capacity of the knapsack.