Sure, here are two implementations of the QuickSort algorithm in Python:

Implementation 1:

```
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        items_greater = []
        items_lower = []
        for item in arr:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        return quickSort(items_lower) + [pivot] + quickSort(items_greater)
```

Implementation 2:

```
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        items_greater = [item for item in arr[1:] if item > pivot]
        items_lower = [item for item in arr[1:] if item <= pivot]
        return quickSort(items_lower) + [pivot] + quickSort(items_greater)
```

Both implementations take a list of integers 'arr' as input parameter and return a sorted list using the QuickSort algorithm.