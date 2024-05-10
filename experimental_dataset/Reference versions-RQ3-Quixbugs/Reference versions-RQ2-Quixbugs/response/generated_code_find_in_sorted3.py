Sure, here's the first program:

```
def find_in_sorted(arr, x):

    def binsearch(arr, x, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binsearch(arr, x, mid+1, end)
        else:
            return binsearch(arr, x, start, mid-1)

    return binsearch(arr, x, 0, len(arr)-1)
```

And here's the second program, which instead uses a while loop:

```
def find_in_sorted(arr, x):

    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return -1
```

Both programs achieve the same intention, which is to implement binary search to find an element 'x' in a sorted list 'arr'. The first program uses a recursive function 'binsearch', while the second program uses a while loop.