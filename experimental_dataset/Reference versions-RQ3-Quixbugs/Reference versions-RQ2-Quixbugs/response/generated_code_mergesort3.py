Here are two Python programs that implement the Merge Sort algorithm to sort a given list of integers:

Program 1:

```python
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
```

Program 2:

```python
def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        result += right
    else:
        result += left
    return result

def mergesort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = mergesort(left)
        right = mergesort(right)
        return merge(left, right)
```

Both programs use the same method name `mergesort()` and the same parameter type (a list of integers `arr`). The only difference is in the implementation of the `merge()` function, which merges the left and right sublists in a sorted order. Program 1 uses a more concise implementation of the `merge()` function, whereas Program 2 uses a more verbose and explicit implementation to achieve the same result.

Both programs have a time complexity of O(n log n), which is the best possible worst-case time complexity for comparison-based sorting algorithms. Therefore, both programs are efficient and widely used for sorting large lists of integers.