Program 1:

```
def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1
    resultIndex = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            resultIndex = mid
            hi = mid - 1
        elif x < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1 

    return resultIndex
```

Program 2:

```
def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1
    resultIndex = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            resultIndex = mid
            hi = mid - 1

    return resultIndex
```

Both programs achieve the same intention in different ways. Program 1 uses binary search to find the lowest index of `x` in `arr`, while Program 2 uses a modified binary search that only updates `resultIndex` when `arr[mid] == x` and continues to search the left side of the list until there is no more occurrence of `x`.