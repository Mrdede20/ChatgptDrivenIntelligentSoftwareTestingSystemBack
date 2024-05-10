Sure, here are the two programs:

Program 1:

```
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = []
    greater = []
    for i in range(1,len(arr)):
        if arr[i] < pivot:
            lesser.append(arr[i])
        else:
            greater.append(arr[i])
    return quicksort(lesser) + [pivot] + quicksort(greater)
```

Program 2:

```
def quicksort(arr):
    def _quicksort(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            _quicksort(arr, low, pivot)
            _quicksort(arr, pivot+1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    _quicksort(arr, 0, len(arr)-1)
    return arr
```

Both of these programs implement the quicksort algorithm in slightly different ways, but achieve the same goal of sorting the input list in O(n log n) time complexity on average. The first program uses a simple recursive approach, while the second program uses a helper function and a more complex partitioning technique to achieve the same result.