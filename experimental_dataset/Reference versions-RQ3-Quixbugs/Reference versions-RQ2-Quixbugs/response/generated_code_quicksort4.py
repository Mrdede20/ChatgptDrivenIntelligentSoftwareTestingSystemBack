Here are two Python programs that achieve the intention of performing a QuickSort on a given list of integers "arr". Both programs use the same method name "quick_sort" and the same parameter type, which is a list of integers "arr".

Program 1: Using list comprehensions and recursion
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
```

Program 2: Using a helper function and iteration
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = choose_pivot(arr)
    left, right = partition(arr, pivot)
    return quick_sort(left) + [pivot] + quick_sort(right)

def choose_pivot(arr):
    return arr[0]

def partition(arr, pivot):
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return left, right
```

Both of these programs use the same basic algorithm for QuickSort, but they implement it in slightly different ways. Program 1 uses list comprehensions and recursion to divide the list into two sub-lists based on the pivot and then recursively apply QuickSort to those sub-lists. Program 2 uses a helper function to choose the pivot and an iteration to partition the list into two sub-lists. Regardless of the implementation details, both programs achieve the same result of sorting the input list of integers "arr".