Here are two possible solutions to implement the QuickSort algorithm in Python:

Solution 1:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
```

Solution 2:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        left = []
        right = []
        for item in arr:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
        return quick_sort(left) + [pivot] + quick_sort(right)
```

Both solutions utilize recursion to sort the sub-lists, but differ slightly in how the pivot element is selected and the sub-lists are partitioned. Solution 1 uses the first element of the list as the pivot and partitions the list with a loop, while Solution 2 pops the last element of the list to use as the pivot and partitions the list with another loop.