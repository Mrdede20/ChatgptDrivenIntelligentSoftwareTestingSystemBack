Here are two Python programs that achieve the given intention using the same method name `bitcount()` and the same parameter type of integer `n`:

Program 1: Using a While Loop
```
def bitcount(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

Program 2: Using Recursion
```
def bitcount(n):
    if n == 0:
        return 0
    else:
        return (n & 1) + bitcount(n >> 1)
```

Both programs follow the same approach of checking the least significant bit of a given number using the bitwise AND operator, and incrementing the count variable if the bit is 1. Then, the number is shifted right by 1 bit to check the next bit, until all bits have been checked. The second program achieves this using recursion, where the base case is when the number becomes 0 and the function returns the count of set bits calculated so far, and the recursive step checks the least significant bit and shifts the number right by one bit before making the recursive call.