
def possible_change(total, coins):
    possibilities = [0] * (total + 1)
    possibilities[0] = 1
    for coin in coins:
        for i in range(coin, total + 1):
            possibilities[i] += possibilities[i - coin]
    return possibilities[total]
