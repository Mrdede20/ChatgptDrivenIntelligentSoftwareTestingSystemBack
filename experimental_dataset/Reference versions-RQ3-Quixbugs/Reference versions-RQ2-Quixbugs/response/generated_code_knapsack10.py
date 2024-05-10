Here are two programs which fulfill the mentioned requirements:

Program 1:

```
from collections import defaultdict

def knapsack(capacity, items):
    memo = defaultdict(int)

    for weight, value in items:
        for i in range(capacity, weight - 1, -1):
            memo[i] = max(memo[i], memo[i - weight] + value)

    return memo[capacity]
```

Program 2:

```
from collections import defaultdict

def knapsack(capacity, items):
    memo = defaultdict(int)

    for idx in range(len(items)):
        weight, value = items[idx]
        for cap in range(weight, capacity + 1):
            memo[cap] = max(memo[cap], memo[cap - weight] + value)

    return memo[capacity]
```

Both programs use dynamic programming approach to solve the knapsack problem. They create a `defaultdict` named `memo` to store the optimal value of the knapsack after examining each combination of items to select. 

The difference between both programs is how they iterate over the items and capacity of the knapsack. Program 1 iterates over the capacity first and then over the items, whereas Program 2 iterates over the items first and then over the capacity. Both approaches are valid and yield the correct result.