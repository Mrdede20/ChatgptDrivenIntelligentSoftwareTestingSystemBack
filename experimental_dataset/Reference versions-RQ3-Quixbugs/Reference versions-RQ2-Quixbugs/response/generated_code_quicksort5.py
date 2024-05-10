Here are two programs that achieve the same intention:

Program 1:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser = []
    greater = []

    for i in arr[1:]:
        if i < pivot:
            lesser.append(i)
        else:
            greater.append(i)

    return quicksort(lesser) + [pivot] + quicksort(greater)
```

Program 2:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]

    return quicksort(lesser) + [pivot] + quicksort(greater)
```

Both of these programs implement the QuickSort algorithm as described in the prompt. They have the same function name (`quicksort`) and parameter type (a list of integers `arr`). The main difference between the two programs is in the way they construct the `lesser` and `greater` lists. 

In program 1, the `lesser` and `greater` lists are constructed using a `for` loop and an `if` statement to check whether each element is less than or greater than the pivot. In program 2, list comprehension is used to construct the `lesser` and `greater` lists based on whether each element is less than or greater than or equal to the pivot.

Both approaches achieve the same end result and have the same time complexity, so it comes down to personal preference and readability.