Sure, here are two sample implementations of the `mergesort` function in Python:

Implementation 1:
```
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_sorted = mergesort(left_half)
    right_sorted = mergesort(right_half)
    return merge(left_sorted, right_sorted)
    
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
```
 
Implementation 2:
```
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergesort(left_half)
        mergesort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr
```

Both implementations take a list `arr` as input and sort it using the merge sort algorithm. The only difference is in how the `merge` operation is implemented. The first implementation uses a separate `merge` function that takes two sorted lists and merges them into a single sorted list. The second implementation does not use a separate function, but instead performs the merging operation within the `mergesort` function itself.