Program 1:

```
def binary_search(arr, x):
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            result = mid
            hi = mid - 1
    return result
```

Program 2:

```
def binary_search(arr, x):
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            result = mid
            lo = mid + 1
    return result
```
Both programs use the same method name `binary_search` and take in two arguments - a sorted array `arr` and a value `x` to be found. The programs return the index of the first occurrence of x in the array or -1 if x is not present in the array. The difference between the programs is in the way they determine whether to continue searching the left or right half of the array once the midpoint is found to be equal to the target value. Program 1 narrows the search to the left half, while Program 2 narrows the search to the right half. This is done to find the first occurrence of x.