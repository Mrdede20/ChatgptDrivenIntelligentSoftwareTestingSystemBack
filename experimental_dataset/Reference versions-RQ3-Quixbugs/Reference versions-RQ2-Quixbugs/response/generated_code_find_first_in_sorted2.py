Here are two programs which achieve the given intention:

Program 1: Using simple binary search
```
def find_first_in_sorted(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            # If we reached the first occurrence of x
            if mid == 0 or arr[mid - 1] != x:
                return mid
            # Else, adjust the high parameter to search lower indices
            else:
                high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

Program 2: Using fancy binary search

```
def find_first_in_sorted(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x and (mid == 0 or x != arr[mid - 1]):
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

Both programs implement the same logic to find the first occurrence of the target element using a binary search algorithm. However, the second program is slightly more compact as it combines the check for the first occurrence of `x` with the binary search condition.