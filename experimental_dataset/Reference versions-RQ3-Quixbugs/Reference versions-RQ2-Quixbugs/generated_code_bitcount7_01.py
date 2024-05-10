
def bitcount(n):
    # handle negative input values
    if n < 0:
        n = 2 ** 32 + n # compute 2's complement representation
        
    count = 0
    while n != 0:
        n ^= n & -n # toggle least significant 1-bit
        count += 1
        
    return count
