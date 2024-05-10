Program 1:

```
def select_items(A, c, d):
    A.sort(reverse=True)
    sum_d = sum(A[:d])
    if sum_d >= c:
        return "Infinity"
    elif A[0] * d < c:
        return "Impossible"
    else:
        l = 1
        r = len(A)
        while l < r:
            mid = (l + r) // 2
            selected = []
            weight = 0
            for i in range(mid):
                selected.append(A[i])
                weight += A[i]
            if weight >= c:
                r = mid
            else:
                l = mid + 1
        return l
```

Program 2: 

```
def select_items(A, c, d):
    A.sort(reverse=True)
    sum_d = sum(A[:d])
    if sum_d >= c:
        print("Infinity")
    elif A[0] * d < c:
        print("Impossible")
    else:
        l = 1
        r = len(A)
        while l < r:
            mid = (l + r) // 2
            selected = []
            weight = 0
            for i in range(mid):
                selected.append(A[i])
                weight += A[i]
            if weight >= c:
                r = mid
            else:
                l = mid + 1
        print(l)
``` 

Both programs take a list of integers `A`, an integer `c`, and an integer `d`. Program 1 returns the minimum number of groups whose sum of members is at least `c`, while Program 2 prints the value of this minimum number.

Both programs follow the same logic for sorting the list, checking for special cases, implementing a binary search, and updating the limits `l` and `r`. The only difference is that Program 1 returns the result while Program 2 prints the result.