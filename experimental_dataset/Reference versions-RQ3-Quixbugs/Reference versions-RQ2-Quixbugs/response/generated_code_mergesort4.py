Program 1:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

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

Program 2:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        temp = [0]*len(arr)

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                temp[k] = left_half[i]
                i += 1
            else:
                temp[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            temp[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            temp[k] = right_half[j]
            j += 1
            k += 1

        for i in range(len(arr)):
            arr[i] = temp[i]

    return arr
```

Both programs implement the Merge Sort algorithm with the same method name and parameter type. Program 1 uses the original approach of modifying the input array in place, while Program 2 creates a temporary array to store the sorted values before copying them back to the input array. Program 2 may have slightly higher space complexity due to the extra temporary array, but it may perform better due to the reduced number of memory writes.