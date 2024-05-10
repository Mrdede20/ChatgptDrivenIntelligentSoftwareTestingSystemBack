
def bitcount(n):
    count = 0 # Initialize count
    while (n != 0):
        n = (n & (n - 1)) # unset the rightmost set bit
        count += 1
    return count
