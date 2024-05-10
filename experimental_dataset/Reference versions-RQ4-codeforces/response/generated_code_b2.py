Program 1:

```python
def largest_ascii(n):
    for i in range(n):
        a = int(input())
        s = input()
        max_ascii = a
        for char in s:
            if ord(char) > max_ascii:
                max_ascii = ord(char)
        print(max_ascii - 96)
```

Program 2:

```python
def largest_ascii(n):
    results = []
    for i in range(n):
        a = int(input())
        s = input()
        max_ascii = a
        for char in s:
            if ord(char) > max_ascii:
                max_ascii = ord(char)
        results.append(max_ascii - 96)
    return results
```

Both programs have the same method name (`largest_ascii`) and parameter type (`n`). The first program prints out the results immediately while the second program stores the results in a list and returns the list at the end. The second program may be more useful if the results are needed later for further processing.