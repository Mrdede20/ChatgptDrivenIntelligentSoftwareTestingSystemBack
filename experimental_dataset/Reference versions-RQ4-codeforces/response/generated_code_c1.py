Program 1:

```
def max_abs_difference(t: int) -> None:
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        mx = [-1, -1]
        for i in range(n):
            if s[i] > s[mx[0]]:
                mx[1] = mx[0]
                mx[0] = i
            elif s[i] > s[mx[1]]:
                mx[1] = i
        for i in range(n):
            if i == mx[0]:
                print(abs(s[i]-s[mx[1]]))
            else:
                print(abs(s[i]-s[mx[0]]))
```

Program 2:

```
def max_abs_difference(t: int) -> None:
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        mx = [-1, -1]
        for i in range(n):
            if s[i] > s[mx[0]]:
                mx[1], mx[0] = mx[0], i
            elif s[i] > s[mx[1]]:
                mx[1] = i
        for i in range(n):
            if i == mx[0]:
                print(abs(s[i]-s[mx[1]]))
            else:
                print(abs(s[i]-s[mx[0]]))
```

Both programs achieve the same functionality. Program 2 uses an optimized method of swapping elements in the `mx` list using tuple packing and unpacking.