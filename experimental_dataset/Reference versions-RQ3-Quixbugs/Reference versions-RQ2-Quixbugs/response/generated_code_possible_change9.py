First program:

```
def count_change(coins, total):
    if total == 0:
        return 1
    elif total < 0 or not coins:
        return 0
    else:
        return count_change(coins[:-1], total) + count_change(coins, total-coins[-1])
```

Second program (optimized for performance):

```
def count_change(coins, total, memo={}):
    if total == 0:
        return 1
    elif total < 0 or not coins:
        return 0
    elif (len(coins), total) in memo:
        return memo[(len(coins), total)]
    else:
        memo[(len(coins), total)] = count_change(coins[:-1], total, memo) + count_change(coins, total-coins[-1], memo)
        return memo[(len(coins), total)]
```

The second program uses memoization to store previously calculated values and reuse them instead of recomputing them, which can improve the performance of the function for larger input values.