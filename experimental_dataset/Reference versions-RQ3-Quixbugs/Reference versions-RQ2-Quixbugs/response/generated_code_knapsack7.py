Here are two Python programs that implement the knapsack algorithm:

Program 1:

```python
def knapsack(capacity, items):
    memo = {}
    for i in range(1, capacity + 1):
        memo[i] = 0
    for item_weight, item_value in items:
        for i in range(capacity, 0, -1):
            if item_weight <= i:
                memo[i] = max(memo[i], memo[i - item_weight] + item_value)
    return memo[capacity]
```

Program 2:

```python
def knapsack(capacity, items):
    memo = {}
    for i in range(1, capacity + 1):
        memo[i] = 0
    for item in items:
        for i in range(capacity, item[0] - 1, -1):
            memo[i] = max(memo[i], memo[i - item[0]] + item[1])
    return memo[capacity]
```

Both programs take a maximum capacity and a list of items as arguments, and return the maximum total value that can be achieved for the given capacity and items. The second program uses a slightly different loop structure, but both programs achieve the same result.