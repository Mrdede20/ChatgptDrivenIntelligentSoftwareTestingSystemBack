
def bitcount(n):
    count = 0 # Initialize count
    while (n):
        n &= (n-1) # clear the rightmost set bit
        count += 1
    return count
