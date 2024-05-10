Sure, here are two programs that achieve the intended functionality using recursion:

Program 1:

```python
def coin_change_count(coins, total):
    if total == 0:
        return 1
    if total < 0 or not coins:
        return 0
    return coin_change_count(coins[:-1], total) + coin_change_count(coins, total - coins[-1])
```

Program 2:

```python
def coin_change_count(coins, total):
    return rec_coin(coins, total, {})

def rec_coin(coins, total, memo):
    if total == 0:
        return 1
    if total < 0 or not coins:
        return 0
    
    if (len(coins), total) in memo:
        return memo[(len(coins), total)]
    
    memo[(len(coins), total)] = rec_coin(coins[:-1], total, memo) + rec_coin(coins, total - coins[-1], memo)
    return memo[(len(coins), total)]
```

Both programs use the same function name (`coin_change_count`) and input parameters (`coins` and `total`). The first program directly calculates the count of valid combinations using recursion, while the second program memoizes the previously calculated results to avoid redundant calculations.