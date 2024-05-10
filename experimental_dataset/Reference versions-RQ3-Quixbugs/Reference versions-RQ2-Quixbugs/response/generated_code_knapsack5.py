Here's the first implementation of `knapsack` function using dynamic programming:

```
from collections import defaultdict

def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(len(items)):
        weight, value = items[i]
        for j in range(capacity + 1):
            if weight > j:
                memo[(i, j)] = memo[(i-1, j)]
            else:
                memo[(i, j)] = max(memo[(i-1, j)], memo[(i-1, j-weight)] + value)

    return memo[(len(items)-1, capacity)]
```

Here's the second implementation of `knapsack` function using recursion:

```
def knapsack(capacity, items):
    def helper(i, j):
        if i < 0 or j == 0:
            return 0
        weight, value = items[i]
        if weight > j:
            return helper(i-1, j)
        else:
            return max(helper(i-1, j), helper(i-1, j-weight) + value)

    return helper(len(items)-1, capacity)
``` 

Both of these functions take in two parameters: `capacity` and `items`, where `items` is a list of tuples representing the weight and value of each item. Both the approaches solve the knapsack problem to maximize the value for the given weight capacity of the knapsack. While the first implementation uses dynamic programming in a bottom-up manner, the second implementation uses recursion in a top-down manner.