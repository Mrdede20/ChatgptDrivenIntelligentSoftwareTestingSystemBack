Here are two programs that implement the QuickSelect algorithm to find the kth smallest element in an array of integers:

Program 1:
```python
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quickselect(right, k - len(left) - len(middle))
```

Program 2:
```python
def quickselect(arr, k):
    low = 0
    high = len(arr) - 1
    while True:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif k < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
```

Both programs have the same method name `quickselect` and parameter type of an array of integers `arr` and an integer `k` representing the kth smallest element to be found. The first program uses list comprehensions to split the array into smaller, equal, and larger sub-arrays, and recursively calls itself on the appropriate sub-array based on the value of `k`. The second program uses a while loop and the partition function to iteratively narrow down the search for the kth smallest element by repeatedly dividing the array into two parts around a pivot element, and only searching in the part that contains the kth smallest element.