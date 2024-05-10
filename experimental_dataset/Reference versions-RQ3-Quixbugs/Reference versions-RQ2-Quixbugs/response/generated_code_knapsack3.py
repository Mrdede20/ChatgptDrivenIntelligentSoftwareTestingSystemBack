Here's the first program:

```
from collections import defaultdict

def knapsack(weights, values, max_weight):
    memo = defaultdict(int)
    n = len(weights)
    
    for i in range(n):
        weight = weights[i]
        value = values[i]
        for capacity in range(max_weight, 0, -1):
            if weight <= capacity:
                memo[capacity] = max(memo[capacity], memo[capacity - weight] + value)
    
    return memo[max_weight]
```

Here's the second program:

```
from collections import defaultdict

def knapsack(weights, values, max_weight):
    memo = defaultdict(int)
    n = len(weights)
    
    for i in range(1, n+1):
        weight = weights[i-1]
        value = values[i-1]
        for capacity in range(1, max_weight+1):
            if weight <= capacity:
                memo[(i, capacity)] = max(memo[(i-1, capacity)], memo[(i-1, capacity-weight)] + value)
            else:
                memo[(i, capacity)] = memo[(i-1, capacity)]
    
    return memo[(n, max_weight)]
```

Both programs have the same name and parameter type. They take in three arguments: a list of weights of items, a list of values of items, and the maximum weight capacity of the knapsack.