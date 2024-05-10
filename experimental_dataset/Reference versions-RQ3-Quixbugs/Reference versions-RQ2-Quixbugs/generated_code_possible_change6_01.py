
def possible_change(total, coins):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(coins) == 0:
        return 0
    return possible_change(total - coins[0], coins) + possible_change(total, coins[1:])
