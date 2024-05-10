Program 1:

```
def max_difference(t, n, s):
    for i in range(t):
        mx = [-1, -1]
        for j in range(n):
            if s[j] > s[mx[0]]:
                mx[1] = mx[0]
                mx[0] = j
            elif s[j] > s[mx[1]]:
                mx[1] = j
        max_diff = abs(s[mx[0]] - s[mx[1]])
        for k in range(n):
            print(abs(s[k]-s[mx[0]]))
```

Program 2:

```
def max_difference(t, n, s):
    for i in range(t):
        mx = [-1, -1]
        for j in range(n):
            if s[j] > s[mx[0]]:
                mx[1] = mx[0]
                mx[0] = j
            elif s[j] > s[mx[1]]:
                mx[1] = j
        max_diff = abs(s[mx[0]] - s[mx[1]])
        for k in range(n):
            print(abs(s[k]-s[mx[0]]))
```
Both programs achieve the given intention using the same method name and parameter type.