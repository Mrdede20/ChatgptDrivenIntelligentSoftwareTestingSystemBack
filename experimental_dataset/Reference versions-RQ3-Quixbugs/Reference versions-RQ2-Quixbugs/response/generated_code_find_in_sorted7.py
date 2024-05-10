Here are two implementations of the `find_in_sorted` function in Python:

First Implementation:
```
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binsearch(mid+1, end)
        else:
            return binsearch(start, mid-1)
    return binsearch(0, len(arr)-1)
```

Second Implementation:
```
def find_in_sorted(arr, x):
    def binsearch(start, end):
        while end >= start:
            mid = (start + end) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    return binsearch(0, len(arr)-1)
```

Both implementations take in a sorted list of integers (`arr`) and a target value (`x`) and return the index of the target value in the list or -1 if the value is not found.

The first implementation uses recursion to perform the binary search, while the second implementation uses a while loop.