Here are two programs that achieve the same intention:

Program 1:

```
def find_alpha_pos(n: int):
    for i in range(n):
        a = int(input())
        s = input()
        max_char = max(s)
        diff = ord(max_char) - 96
        print(diff)
```

Program 2:

```
def find_alpha_pos(n: int):
    for i in range(n):
        a = int(input())
        s = input()
        max_val = 0
        for char in s:
            val = ord(char)
            if val > max_val:
                max_val = val
        diff = max_val - 96
        print(diff)
```

Both of these programs take an integer parameter `n` as input, which represents the number of test cases. They then use a loop to iterate through each test case and perform the necessary calculations. The first program uses the built-in `max` function to find the highest ASCII value character, while the second program uses a loop to compare the ASCII value of each character. Finally, both programs calculate the difference between the highest ASCII value character and the ASCII value of 'a' and print the result.