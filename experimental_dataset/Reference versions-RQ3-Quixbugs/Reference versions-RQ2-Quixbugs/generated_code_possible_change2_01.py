
def count_change(total, coins):
    if total == 0:
        return 1
    elif not coins or total < 0:
        return 0
    else:
        return count_change(total - coins[0], coins) + count_change(total, coins[1:])
