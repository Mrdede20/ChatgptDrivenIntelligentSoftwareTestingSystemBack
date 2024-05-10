Here are two programs that achieve the given intention with the same function name and parameter type:

Program 1: Using List Comprehension and Recursion

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)
```

In this program, we use list comprehension to create two sub-arrays - `lesser` and `greater`. Then we recursively call the `quicksort()` function on each sub-array and combine them with the pivot element to get the sorted array.

Program 2: Using Divide and Conquer Strategy

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)
```

In this program, we use the divide and conquer strategy. We select the pivot element as the middle element and create three sub-arrays - `left`, `middle` and `right`. Then we recursively call the `quicksort()` function on `left` and `right` sub-arrays, and combine them with the `middle` sub-array to get the sorted array.