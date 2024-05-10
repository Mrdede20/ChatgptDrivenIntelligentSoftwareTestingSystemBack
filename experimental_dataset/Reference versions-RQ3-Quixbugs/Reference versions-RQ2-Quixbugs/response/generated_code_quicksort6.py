Sure, here are two Python programs that implement the QuickSort algorithm for sorting a list of integers in ascending order. Both programs use the same method name and parameter type, as requested.

Program 1:

```
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)
```

Program 2:

```
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        left = []
        right = []
        for element in arr:
            if element < pivot:
                left.append(element)
            else:
                right.append(element)
        return quicksort(left) + [pivot] + quicksort(right)
```

Both programs have the same algorithmic flow:

1. Check the length of the input list. If it is less than or equal to 1, then it is already sorted, so return the list.
2. Select a pivot element. In Program 1, the first element of the list is selected as the pivot. In Program 2, the last element of the list is selected.
3. Partition the list into two sub-lists, one with elements less than the pivot and one with elements greater than the pivot.
4. Recursively sort the sub-lists by calling the `quicksort` function on them.
5. Concatenate the sorted sub-lists along with the pivot element to obtain the final sorted list.

Both programs satisfy the intention of the given code. However, Program 2 uses the `pop` method to remove the last element from the list and use it as the pivot element, whereas Program 1 always selects the first element as the pivot. The choice of pivot element can affect the efficiency of the algorithm in certain cases, but both programs should work well for most input arrays.