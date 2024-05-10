Program 1:

```
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])
    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    i = 0
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    result += left_half[i:]
    result += right_half[j:]
    return result
```

Program 2:

```
def mergesort(arr):
    def merge(left_half, right_half):
        result = []
        i = 0
        j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1
        result += left_half[i:]
        result += right_half[j:]
        return result

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])
    return merge(left_half, right_half)
```

Both programs implement the Merge Sort algorithm using the same function name 'mergesort' and the same parameter type. The first program defines the 'merge' function outside the 'mergesort' function, while the second program defines it inside the 'mergesort' function as an inner function. The rest of the code is the same in both programs, and they have a time complexity of O(nlogn).