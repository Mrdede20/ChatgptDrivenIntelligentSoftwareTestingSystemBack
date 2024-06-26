Here are two programs that achieve the given intention:

Program 1:

```
def decimalToBase(num: int, b: int) -> str:
    digits = '0123456789ABCDEF'
    result = ''
    if num == 0:
        return '0'
    while num > 0:
        digit = digits[num % b]
        result = digit + result
        num = num // b
    return result
```

Program 2:

```
def decimalToBase(num: int, b: int) -> str:
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    if num == 0:
        return '0'
    while num > 0:
        digit = digits[num % b]
        result = digit + result
        num = num // b
    return result
```

Both programs take in the same parameters: `num` (the decimal number to be converted) and `b` (the base to be converted to) and return the result string. They use the same method name `decimalToBase`. 

The main difference between these two programs is that the first program uses base 16 (hexadecimal) and the second program uses base 36 (using letters A-Z in addition to digits 0-9). 

Both programs create a string that contains all of the needed digits and letters for the given base and use this to construct the output string. The result is generated by continuously taking the modulo of the input number (num) with the target base (b) and adding the corresponding digit to a string, until the input number becomes zero.