Sure! Here are two Python programs which both implement the binary search algorithm using a recursive function called `binsearch` with the same parameters:

Program 1:

```python
def binsearch(arr, x, start, end):
    if start > end:
        return -1
        
    mid = (start + end) // 2
    
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binsearch(arr, x, mid + 1, end)
    else:
        return binsearch(arr, x, start, mid - 1)
```

Program 2:

```python
def binsearch(arr, x, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
            
    return -1
```

Both programs work by continually dividing the search interval in half and checking the middle element until the target element is found or the interval becomes empty. The first program uses recursion to achieve this while the second program uses a while loop.