Program 1:

```
def modified_binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid-1] != x:
                return mid
            else:
                high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

Program 2:

```
def modified_binary_search(arr, x):
    def recurse(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid-1] != x:
                return mid
            else:
                return recurse(low, mid-1)
        elif arr[mid] < x:
            return recurse(mid+1, high)
        else:
            return recurse(low, mid-1)
    return recurse(0, len(arr)-1)
```

Both programs use the same method name `modified_binary_search` and take the same parameters `arr` and `x`. They use a modified binary search algorithm to find the lowest index of `x` in `arr`, or return -1 if `x` is not found. The modification checks if `mid` is the first occurrence of `x` in the array by verifying if the previous value (at index `mid-1`) is not equal to `x`.