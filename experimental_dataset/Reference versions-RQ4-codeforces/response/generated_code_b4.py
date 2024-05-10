Program 1:

```python
def ascii_position(n):
    a = 0
    for i in range(n):
        a=int(input())
        s=input()
        max_char = chr(a)
        for i in range(len(s)):
            if ord(s[i]) > a and ord(s[i]) > ord(max_char):
                max_char = s[i]
        print(ord(max_char) - 96)
```

Program 2:

```python
def ascii_position(n):
    for i in range(n):
        a, s = input().split()
        a = int(a)
        max_char = chr(a)
        for i in range(len(s)):
            if ord(s[i]) > a and ord(s[i]) > ord(max_char):
                max_char = s[i]
        print(ord(max_char) - 96)
```

Both programs use the same method name `ascii_position` and take an integer `n` as input, followed by `n` pairs of inputs, where each pair consists of an integer `a` and a string `s`. The programs determine the ASCII value of the highest character in the string `s` that is greater than the integer `a` and print its position in the alphabets (i.e. its value minus 96).

Program 1 takes integer `a` and string `s` as separate inputs inside the for loop, while Program 2 takes both inputs together as a single string input which is then split into two using the `split()` function.