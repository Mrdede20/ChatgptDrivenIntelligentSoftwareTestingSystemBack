
def bitcount(n):
    count = 0
    while n:
        count += 1
        n = n & (n-1)
    return count

# Test Cases
print(bitcount(0))  # 0
print(bitcount(7))  # 3
print(bitcount(100))  # 3
print(bitcount(512))  # 1
print(bitcount(1023))  # 10
