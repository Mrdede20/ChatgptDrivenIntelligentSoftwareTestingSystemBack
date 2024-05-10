Sure, here are two programs that achieve the same intention:

Program 1:

```python
def find_max_ascii(n: int) -> None:
    for i in range(n):
        a = int(input())
        s = input().strip()
        max_ascii = max(ord(char) for char in s)
        result = max_ascii - 96
        print(result)
```

Program 2:

```python
def find_max_ascii(n: int) -> None:
    import string

    for i in range(n):
        a = int(input())
        s = input().strip()
        max_char = max(s.lower())
        result = string.ascii_lowercase.index(max_char) + 1
        print(result)
```

Both programs achieve the same intention of finding the maximum ASCII value of the characters in the input string and subtracting 96 from it to get the position of the highest letter in the alphabet (ignoring case). Program 1 achieves this by using the built-in `ord` function to get the ASCII value of each character in the string and finding the maximum value using the `max` function. Program 2 achieves this by converting the entire string to lowercase, finding the maximum character using the `max` function, and then using the `index` method of the `string.ascii_lowercase` string to find the position of the maximum character in the alphabet.