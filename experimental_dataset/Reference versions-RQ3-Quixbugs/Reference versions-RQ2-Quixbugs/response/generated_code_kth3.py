Sure! Here are two programs that achieve this intention using the QuickSelect algorithm:

Program 1:

```python
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    else:
        pivot = arr[0]
        lows = [elem for elem in arr if elem < pivot]
        highs = [elem for elem in arr if elem > pivot]
        pivots = [elem for elem in arr if elem == pivot]

        if k < len(lows):
            return quickselect(lows, k)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots))
```

Program 2:

```python
def quickselect(arr, k):
    """Find the kth lowest element in a given list of integers."""
    if len(arr) == 1:
        return arr[0]

    pivot = arr[0]
    lows = [elem for elem in arr if elem < pivot]
    highs = [elem for elem in arr if elem > pivot]
    pivots = [elem for elem in arr if elem == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))
```

Both programs have the same method name `quickselect` and the same parameter type `arr` (a list of integers) and `k`. They use list comprehension to partition the list into lower and higher elements, and recursively call the function until the kth lowest element is found. The pivot element is selected as the first element.