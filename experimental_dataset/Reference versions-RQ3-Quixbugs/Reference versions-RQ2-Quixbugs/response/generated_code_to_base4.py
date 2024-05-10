Here are two programs that achieve the above intention:

Program 1:

```python
import string

def to_base(num, b):
    if not isinstance(b, int) or b < 2 or b > 36:
        raise ValueError("Base must be an integer between 2 and 36")
    if not isinstance(num, int) or num < 0:
        raise ValueError("Number must be a positive integer")
    alphabet = string.digits + string.ascii_uppercase
    result = ''
    while num > 0:
        num, remainder = divmod(num, b)
        result += alphabet[remainder]
    return result[::-1] if result else '0'
```

Program 2:

```python
import string

def to_base(num, b):
    if not isinstance(b, int) or b < 2 or b > 36:
        raise ValueError("Base must be an integer between 2 and 36")
    if not isinstance(num, int) or num < 0:
        raise ValueError("Number must be a positive integer")
    alphabet = string.digits + string.ascii_uppercase
    result = []
    while num > 0:
        num, remainder = divmod(num, b)
        result.append(alphabet[remainder])
    return ''.join(reversed(result)) if result else '0'
```

Both programs take two parameters - `num` and `b`, where `num` is the number to be converted and `b` is the target base. The programs use the same algorithm to convert the number to the target base and return the result as a string.

The difference between the programs is in how the result is constructed. Program 1 uses string concatenation to build the result in reverse order, while Program 2 uses a list to accumulate the characters and then joins them in reverse order at the end.