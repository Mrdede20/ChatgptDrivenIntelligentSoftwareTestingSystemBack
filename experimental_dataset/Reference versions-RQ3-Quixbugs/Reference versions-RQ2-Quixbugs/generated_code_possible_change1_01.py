
def count_change(total, coins):
    if total == 0:
        return 1
    if total < 0 or len(coins) == 0:
        return 0
    return count_change(total - coins[0], coins) + count_change(total, coins[1:])
