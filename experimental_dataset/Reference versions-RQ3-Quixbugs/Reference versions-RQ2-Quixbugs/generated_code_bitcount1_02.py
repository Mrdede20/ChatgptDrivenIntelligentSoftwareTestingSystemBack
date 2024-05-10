
def bitcount(n):
    if n == 0:
        return 0
    else:
        return (n & 1) + bitcount(n >> 1)
