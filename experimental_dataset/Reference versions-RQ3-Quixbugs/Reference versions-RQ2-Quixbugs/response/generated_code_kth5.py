Here are two programs that achieve the desired outcome:

Program 1:

```python
def kth(arr, k):
    if arr:
        pivot = arr[0]
        smaller = [x for x in arr if x < pivot]
        bigger = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]
        if k < len(smaller):
            return kth(smaller, k)
        elif k < len(smaller) + len(pivots):
            return pivots[0]
        else:
            return kth(bigger, k - len(smaller) - len(pivots))
```

Program 2:

```python
def kth(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    if k <= len(left):
        return kth(left, k)
    else:
        return kth(right, k - len(left))
```

Both of these programs implement the QuickSelect algorithm to efficiently find the kth-lowest element of a list of integers. The first program uses list comprehension to create the smaller, bigger, and pivots lists, while the second program uses list slices to create the left and right lists. Both programs are recursive and call themselves with the appropriate sublist, depending on the value of k.