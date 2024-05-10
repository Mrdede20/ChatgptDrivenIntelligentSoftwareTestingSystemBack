
def count_change(total, denominations):
    if total == 0:
        return 1
    if total < 0 or not denominations:
        return 0
    return count_change(total - denominations[0], denominations) + count_change(total, denominations[1:])
