Program 1:

```
def bitcount(n):
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count

# Test Cases
print(bitcount(0))  # 0
print(bitcount(7))  # 3
print(bitcount(100))  # 3
print(bitcount(512))  # 1
print(bitcount(1023))  # 10
```

Program 2:

```
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
```
Both programs use different techniques to count the number of 1-bits in the binary encoding of `n`. The first program uses a right shift and bitwise AND operation, whereas the second program uses bitwise AND and subtraction. The outputs should be the same for all the provided test cases.