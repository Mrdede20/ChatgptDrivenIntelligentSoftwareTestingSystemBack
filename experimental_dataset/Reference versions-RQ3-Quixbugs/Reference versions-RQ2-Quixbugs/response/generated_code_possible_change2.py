Sure, here are two programs that achieve the given intention:

Program 1: 

```
def count_change(total, coins):
    if total == 0:
        return 1
    elif not coins or total < 0:
        return 0
    else:
        return count_change(total - coins[0], coins) + count_change(total, coins[1:])
```

Program 2:

```
def count_change(total, coins):
    def helper(total, coins, i):
        if total == 0:
            return 1
        elif i >= len(coins) or total < 0:
            return 0
        else:
            return helper(total - coins[i], coins, i) + helper(total, coins, i+1)
    return helper(total, coins, 0)
```

Both programs have the same function name "count_change" and take in two parameters: "total" and "coins". The function first checks if the total is zero, in which case there is only one way to make change - using no coins. If there are no coins or the total is negative, then there are no ways to make change. 

In Program 1, the function simply calls itself recursively for the remaining denominations, adding up the total count for each denomination. The base case is when the total becomes zero.

In Program 2, the function uses a helper function that takes an additional parameter "i", which is used to keep track of the current coin denomination being considered. The helper function recursively calls itself with the remaining denominations, and the base case is the same as in Program 1. The main function "count_change" simply calls the helper function with the initial values of "total", "coins", and "i".