
def bitcount(n):
    # handle negative input values
    if n < 0:
        n = 2 ** 32 + n # compute 2's complement representation
        
    count = 0
    while n:
        count += 1
        n &= n - 1 # clear least significant 1-bit
        
    return count
