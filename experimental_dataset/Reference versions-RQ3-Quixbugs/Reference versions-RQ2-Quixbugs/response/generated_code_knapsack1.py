Sure, here are two possible implementations:

Implementation 1:

```
from collections import defaultdict

def knapsack(capacity, items):
    dp = defaultdict(int)
    for i in range(len(items)):
        for w in range(capacity+1):
            if items[i][0] <= w:
                dp[(i, w)] = max(dp[(i-1, w)], dp[(i-1, w-items[i][0])] + items[i][1])
            else:
                dp[(i, w)] = dp[(i-1, w)]
    return dp[(len(items)-1, capacity)]
```

Implementation 2:

```
from collections import defaultdict

def knapsack(capacity, items):
    dp = defaultdict(int)
    for item, value in items:
        for w in range(capacity+1):
            if item <= w:
                dp[w] = max(dp[w], dp[w-item] + value)
    return dp[capacity]
```

Both implementations use the same method name and input parameters (i.e. `knapsack(capacity, items)`). 

The first implementation uses a dictionary to store the maximum value of the knapsack for each (item, capacity) pair, and updates the values iteratively by considering the previously computed values. The second implementation uses a dictionary to store the maximum value of the knapsack for each possible capacity, and updates the values by considering the previously computed values for smaller capacities. 

Both implementations have a time complexity of O(nW), where n is the number of items and W is the maximum capacity of the knapsack.