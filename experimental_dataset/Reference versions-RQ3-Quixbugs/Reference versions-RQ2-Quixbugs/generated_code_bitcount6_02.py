
def bitcount(n):
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count

# test cases
assert bitcount(0) == 0
assert bitcount(1) == 1
assert bitcount(2) == 1
assert bitcount(7) == 3
assert bitcount(256) == 1
