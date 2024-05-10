Here are two Python programs that implement the binary search algorithm:

Program #1:

```python
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

Program #2 (Recursive):

```python
def binary_search(arr, x, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search(arr, x, mid + 1, high)
    else:
        return binary_search(arr, x, low, mid - 1)
``` 

Both implementations have the same signature, i.e., same method name and parameter type. The first program uses a while loop to search for the target value by dividing the list in half until the target is found or determined to not be in the list. The second program uses recursion to achieve the same result. Both implementations are optimized by continuously halving the list until an answer is found, reducing the time complexity from O(n) to O(log n).