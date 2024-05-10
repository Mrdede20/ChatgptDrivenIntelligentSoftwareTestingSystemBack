Here are two implementations of the QuickSort algorithm in Python:

### First implementation:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

### Second implementation:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort(left) + [pivot] + quicksort(right)
```

Both implementations work in the same way by recursively partitioning and sorting the input list. The first implementation chooses the pivot element as the middle element in the list, while the second implementation chooses the first element as the pivot. Both implementations have a base case that is reached when the input list has zero or one elements, in which case the input list is returned as output.