Here are two different implementations of the binary search algorithm with the same method name and parameter type:

1) Implementation using recursion:

```
def binary_search(arr, x, start, end):
    if end >= start:
        mid = start + (end - start) // 2
        
        if arr[mid] == x:
            if mid == start or arr[mid-1] != x:
                return mid
            else:
                return binary_search(arr, x, start, mid-1)
        
        elif arr[mid] > x:
            return binary_search(arr, x, start, mid-1)
        
        else:
            return binary_search(arr, x, mid+1, end)
    
    else:
        return -1
```

2) Implementation using a while loop:

```
def binary_search(arr, x):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] == x:
            if mid == start or arr[mid-1] != x:
                return mid
            else:
                end = mid - 1
        
        elif arr[mid] > x:
            end = mid - 1
        
        else:
            start = mid + 1
    
    return -1
```

Both implementations perform the binary search on a sorted list of integers to find the index of the first occurrence of a given value 'x'. The first implementation uses recursion to perform the search, while the second implementation uses a while loop. They have the same method name `binary_search` and the same parameter type `arr` and `x`.