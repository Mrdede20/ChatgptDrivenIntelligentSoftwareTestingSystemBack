Program 1:

```
import string

def to_base(num, b):
    if num < 0:
        return '-' + to_base(-num, b)
    alphabet = string.digits + string.ascii_uppercase
    result = ''
    while num:
        num, rem = divmod(num, b)
        result = alphabet[rem] + result
    return result or '0'
```

Program 2:

```
import string

def to_base(num, b):
    if num == 0:
        return "0"
    elif num < 0:
        return "-" + to_base(-1*num, b)
    else:
        result = ""
        alphabet = string.digits + string.ascii_uppercase
        while num > 0:
            rem = num % b
            result = alphabet[rem] + result
            num = num // b
        return result
```

Both programs implement the same function called `to_base`, and take the arguments "num" and "b" as described. Both programs use the "string" module to define the alphabet variable containing digits and uppercase letters to represent remainders in the target base. Both programs use a while loop to divide the integer by the target base and add the remainders to the result string, and return the result string as the output. The first program includes an additional case to handle negative input integers. Program 2 handles both positive and negative integers.