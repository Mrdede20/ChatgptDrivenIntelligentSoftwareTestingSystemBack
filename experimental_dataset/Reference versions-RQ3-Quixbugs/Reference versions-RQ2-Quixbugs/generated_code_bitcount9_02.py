
def bitcount(n):
    if n < 0:
        return 0
    count = 0
    while n != 0:
        n ^= n - 1
        count += 1
    return count
