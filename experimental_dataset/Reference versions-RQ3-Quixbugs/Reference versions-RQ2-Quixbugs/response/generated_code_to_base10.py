Here are two possible solutions to achieve this intention:

Solution 1:

```python
import string

def to_base(num, b):
    digits = string.digits + string.ascii_uppercase
    result = ""
    while num:
        num, rem = divmod(num, b)
        result += digits[rem]
    return result[::-1] if result else digits[0]
```

Solution 2:

```python
import string

def to_base(num, b):
    digits = string.digits + string.ascii_uppercase
    if num < b:
        return digits[num]
    else:
        return to_base(num//b, b) + digits[num%b]
```

Both solutions implement the same algorithm using different approaches. The first solution uses a loop to perform repeated division with remainder and build the result string in reverse order, while the second solution uses recursion to build the result string from the remainders of the divisions in the correct order. The choice between the two solutions depends on personal preference and coding style. Both solutions should give the same correct result for any given input.