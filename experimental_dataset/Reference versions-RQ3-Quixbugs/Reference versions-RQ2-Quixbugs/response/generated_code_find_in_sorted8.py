Here is the first program:

```
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if end >= start:
            mid = start + (end - start) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binsearch(start, mid - 1)
            else:
                return binsearch(mid + 1, end)
        else:
            return -1

    return binsearch(0, len(arr) - 1)
```

Here is the second program which uses an iterative approach instead of recursion:

```
def find_in_sorted(arr, x):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1
```

Both programs share the same function name `find_in_sorted` and parameter type `(arr, x)`. The first program uses recursion while the second one is iterative.