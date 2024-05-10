Here is the first program:

```
def calculate_ascii(n):
    for i in range(n):
        s, num = input().split()
        max_ascii = 0
        for c in s:
            if ord(c) > max_ascii:
                max_ascii = ord(c)
        result = max_ascii - 96
        print(result)
```

Here is the second program:

```
def calculate_ascii(n):
    for i in range(n):
        s, num = input().split()
        max_ascii = max(list(map(ord, s)))
        result = max_ascii - 96
        print(result)
```

Both programs achieve the same intention. The programs take an integer input 'n' and then take 'n' number of inputs where each input is a string and an integer. The program then iterates through each string input and finds the ASCII value of the highest character in the string. Finally, it subtracts 96 from the highest ASCII value because the lowercase English alphabets start from ASCII value 97 and ends at ASCII value 122 and prints the result.