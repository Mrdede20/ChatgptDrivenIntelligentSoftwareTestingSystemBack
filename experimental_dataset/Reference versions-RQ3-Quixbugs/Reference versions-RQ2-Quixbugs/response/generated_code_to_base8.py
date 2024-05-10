First Program:

```python
def to_base(num: int, b: int) -> str:
    if num < 0 or b < 2:
        raise ValueError("Invalid input: num must be non-negative and b must be greater than or equal to 2.")
    result = ""
    alphabet = "0123456789ABCDEF"
    while num > 0:
        remainder = num % b
        result = alphabet[remainder] + result
        num //= b
    return result
```

This implementation includes preconditions for the input `num` and `b` and uses the while loop to repeatedly divide `num` by `b`, append the remainder to the `result` string variable, and update `num` by integer division with `b`.

Second Program:

```python
def to_base(num: int, b: int) -> str:
    if num < 0 or b < 2:
        raise ValueError("Invalid input: num must be non-negative and b must be greater than or equal to 2.")
    result = ""
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while num > 0:
        remainder = num % b
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = alphabet[remainder - 10] + result
        num //= b
    return result
```

This implementation is similar to the first one, except that it uses a different `alphabet` string variable to handle the possibility of a target base greater than 16. If the remainder is less than 10, it simply appends it as a string to the `result` variable. Otherwise, it uses a corresponding digit or letter from the `alphabet` string variable.