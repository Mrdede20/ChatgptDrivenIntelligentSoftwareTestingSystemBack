Sure, here are two programs that fulfill this intention:

Program 1:
```python
def to_base(num, b):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return "0"
    base_b_num = ""
    while num != 0:
        rem = num % b
        base_b_num = alphabet[rem] + base_b_num
        num //= b
    return base_b_num
```


Program 2:
```python
def to_base(num, b):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base_b_num = ""
    while num != 0:
        rem = num % b
        base_b_num = alphabet[rem] + base_b_num
        num //= b
    return "0" if base_b_num == "" else base_b_num
```

Both programs take in two arguments, `num` (the base-10 integer to convert) and `b` (the target base to convert `num` to). They use a string `alphabet` that contains the characters to represent each digit/letter in the target base. 

The conversion algorithm works as follows: 

1. If `num` is 0, return "0" (this is a special case).
2. Initialize an empty string `base_b_num` to store the result of the conversion. 
3. We repeatedly divide `num` by `b` and store the remainder. The remainder must be used to look up the corresponding character in the `alphabet` string. The remainder is also used to update `num`.
4. The loop continues until `num` becomes 0.
5. Finally, we return the resulting `base_b_num` string, which represents `num` in the target base `b`. In Program 2, if the resulting `base_b_num` string is empty, we return "0" instead..

Note that Program 2 has an additional check to return "0" as the result if `num` is 0.