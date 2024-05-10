Sure, here are two examples:

Example 1:

```python
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1
        if arr[mid] == x:
            index = mid
    return index
```

Example 2:

```python
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            index = mid
            right = mid - 1
    return index
```

Both of these algorithms use binary search to find the leftmost occurrence of `x` in the sorted list `arr`. The first example updates both the left and right indexes while the second example only updates the left index when the current middle value is less than `x`.