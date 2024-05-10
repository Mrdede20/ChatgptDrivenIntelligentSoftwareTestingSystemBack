Program 1:

```
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
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

Program 2:

```
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    i = j = 0
    sorted_arr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr += left[i:]
    sorted_arr += right[j:]
    return sorted_arr
```

Both of these programs achieve the intention of performing merge sort on a list of integers by recursively dividing the input list into halves until each half has only one element or is empty. Then it combines the sorted halves by comparing the elements of both halves and inserting them in the correct order, to produce the final sorted list.