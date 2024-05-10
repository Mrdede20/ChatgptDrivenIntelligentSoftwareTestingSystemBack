Here are two possible versions of the program:

Version 1:

```python
def find_in_sorted(arr, value):

    def binsearch(start, end):

        if start > end:
            return -1

        mid = (start + end) // 2

        if arr[mid] == value:
            return mid

        elif arr[mid] > value:
            return binsearch(start, mid-1)

        else:
            return binsearch(mid+1, end)

    return binsearch(0, len(arr)-1)
```

Version 2:

```python
def find_in_sorted(arr, value):

    def binsearch(start, end):

        while start <= end:

            mid = (start + end) // 2

            if arr[mid] == value:
                return mid

            elif arr[mid] > value:
                end = mid - 1

            else:
                start = mid + 1

        return -1

    return binsearch(0, len(arr)-1)
```

Both versions accomplish the same task of performing a binary search on a sorted list of integers to find the index of a given value. They take in two parameters, an array of sorted integers and the value to search for. They define a nested binsearch function which performs the recursive (version 1) or iterative (version 2) binary search algorithm on the array to find the index of the given value. If the value is not found in the array, they both return -1. The function returns the result of calling the binsearch function with the start and end indices of the array.