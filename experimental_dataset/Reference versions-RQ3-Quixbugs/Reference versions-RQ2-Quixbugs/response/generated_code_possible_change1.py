Program 1:

```python
def count_change(total, coins):
    if total == 0:
        return 1
    if total < 0 or len(coins) == 0:
        return 0
    return count_change(total - coins[0], coins) + count_change(total, coins[1:])
```

Program 2:

```python
def count_change(total, coins):
    memo = {}
    
    def count_helper(total, coins):
        if (total, len(coins)) in memo:
            return memo[(total, len(coins))]
        if total == 0:
            return 1
        if total < 0 or len(coins) == 0:
            return 0
        result = count_helper(total - coins[0], coins) + count_helper(total, coins[1:])
        memo[(total, len(coins))] = result
        return result
    
    return count_helper(total, coins)
```

Both programs take in two parameters - the total amount to be made up and a list of coin denominations. They both use recursion to find the number of distinct ways to make change for the given total, but Program 2 uses memoization to optimize the function by storing previously calculated values and using them instead of recalculating every time.