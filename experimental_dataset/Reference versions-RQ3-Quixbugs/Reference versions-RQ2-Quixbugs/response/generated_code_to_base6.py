Here are two implementations of the `to_base()` function:

Implementation 1:

```python
def to_base(num, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num > 0:
        remainder = num % b
        result = digits[remainder] + result
        num //= b
    return result if result != "" else "0"
```

Implementation 2:

```python
def to_base(num, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    if num == 0:
        return "0"
    while num > 0:
        rem = num % b
        result += digits[rem]
        num = num // b
    return result[::-1]
```

Both implementations take the same two arguments `num` and `b`, and return a string representation of the `num` converted to the target base `b`. They also use the same approach of initializing an empty string `result`, an alphabet string, and using a loop to iterate until `num` is greater than zero.

The difference between the two implementations is how they handle edge cases. Implementation 1 returns `"0"` for input `num = 0, b = any`, while Implementation 2 has a conditional statement to handle this edge case. Additionally, Implementation 2 appends the characters to `result` in the loop and then reverses the resulting string before returning it. This is done to ensure that the string is in the correct order since the characters are added to `result` in reverse order.