Here are two programs that achieve the intention:

Program 1:
```
def find_max_unicode(n: int) -> None:
    for i in range(n):
        a, s = map(str,input().split())
        max_unicode = 0
        for j in range(len(s)):
            if ord(s[j]) > max_unicode:
                max_unicode = ord(s[j])
        print(max_unicode-96)
```

Program 2:
```
def find_max_unicode(n: int) -> None:
    for i in range(n):
        a, s = input().split()
        max_unicode = max(map(ord, s))
        print(max_unicode-96)
```

Both programs have the same method name and parameter type and achieve the same goal. Program 1 uses a for loop to iterate through each character in the string 's' and find the one with the highest Unicode value, while Program 2 uses the built-in 'max' function with a 'map' function to find the max Unicode value directly.