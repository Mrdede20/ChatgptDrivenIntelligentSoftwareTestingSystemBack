
def count_change(coins, total):
    if total == 0:
        return 1
    elif total < 0 or not coins:
        return 0
    else:
        return count_change(coins[:-1], total) + count_change(coins, total-coins[-1])
