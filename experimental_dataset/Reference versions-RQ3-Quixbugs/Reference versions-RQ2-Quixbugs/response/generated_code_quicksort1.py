Sure, here are two programs that implement the QuickSort algorithm in Python:

Program 1:
```
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)
```

Program 2:
```
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        lesser = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(lesser) + equal + quicksort(greater)
```

Both programs take a list `arr` as input and recursively partition and sort it using the QuickSort algorithm. The first program uses the first element of the list as the pivot element, while the second program uses the middle element. The resulting sorted list is returned.