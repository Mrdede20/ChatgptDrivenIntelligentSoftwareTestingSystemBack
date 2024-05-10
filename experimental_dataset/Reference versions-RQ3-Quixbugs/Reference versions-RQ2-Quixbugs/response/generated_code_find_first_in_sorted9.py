Sure, here are two implementations of `find_first_in_sorted`:

First Implementation:

```python
def find_first_in_sorted(arr, x):
    lo, hi = 0, len(arr) - 1
    result = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == x:
            result = mid
            hi = mid - 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            lo = mid + 1

    return result
```

Second Implementation:

```python
def find_first_in_sorted(arr, x):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo if lo < len(arr) and arr[lo] == x else -1
```

Both implementations use the same parameters and binary search algorithm to find the first occurrence of `x` in the sorted `arr` array. The first implementation uses a variable `result` to store the index of the first occurrence of the element `x` and updates the `hi` pointer to search for any earlier occurrences of `x`. The second implementation uses the `lo` pointer to keep track of the lowest index of `x` found so far and returns it if it matches the value of `x` in the end. The second implementation also uses a different condition to check if it has found the element `x`.