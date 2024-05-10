
def count_change(total, coins):
    def helper(total, coins, i):
        if total == 0:
            return 1
        elif i >= len(coins) or total < 0:
            return 0
        else:
            return helper(total - coins[i], coins, i) + helper(total, coins, i+1)
    return helper(total, coins, 0)
