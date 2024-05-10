Here are two possible implementations of the `find_in_sorted` function:

Implementation 1: 

```python
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if end >= start:
            mid = start + (end - start) // 2
            if arr[mid] == x:
                return (mid)
            elif arr[mid] > x:
                return binsearch(start, mid - 1)
            else:
                return binsearch(mid + 1, end)
        else:
            return -1

    return binsearch(0, len(arr) - 1)
```

Implementation 2:

```python
def find_in_sorted(arr, x):
    def binsearch(start, end):
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            if start == end:
                return -1
            return binsearch(start, mid)
        else:
            if start == end:
                return -1
            return binsearch(mid + 1, end)

    return binsearch(0, len(arr) - 1)
```
Both implementations have the same function name, parameter types, and follow the binary search algorithm to find an element in a sorted list.