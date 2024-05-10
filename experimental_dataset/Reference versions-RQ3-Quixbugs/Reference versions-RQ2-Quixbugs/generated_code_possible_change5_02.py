
def coin_change(coins, total):
    def count(coins, m, total):
        if total == 0:
            return 1
        if total < 0:
            return 0
        if m <= 0 and total >= 1:
            return 0
        return count(coins, m-1, total) + count(coins, m, total - coins[m-1])
    return count(coins, len(coins), total)
