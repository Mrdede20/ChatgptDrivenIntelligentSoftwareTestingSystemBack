Sure, here are two possible implementations of the "to_base" function:

Implementation 1:

```python
def to_base(num, b):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num > 0:
        remainder = num % b
        num //= b
        result = alphabet[remainder] + result
    return result
```

Implementation 2:

```python
def to_base(num, b):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while num > 0:
        remainder = num % b
        num //= b
        result.append(alphabet[remainder])
    return ''.join(result[::-1])
```

Both implementations follow the same logic described in the intention. They initialize an empty string or list to store the result, use a while loop to convert each digit of the given number into the target base, and return the resulting string.

The first implementation uses string concatenation to build the result string, while the second implementation appends characters to a list and then joins them together. The second implementation also reverses the list using slicing to get the final result in the correct order.

You can use either of these implementations to perform integer base conversion from base-10 to another base from 2 to 36.