Here are two programs that implement the `find_in_sorted` function using recursion:

Program 1:

```python
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binsearch(start, mid-1)
        else:
            return binsearch(mid+1, end)

    return binsearch(0, len(arr)-1)
```

Program 2:

```python
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            if arr[start] == x:
                return start
            else:
                return -1
        else:
            mid = (start + end) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binsearch(start, mid-1)
            else:
                return binsearch(mid+1, end)

    return binsearch(0, len(arr)-1)
```

Both programs are essentially the same, with the only difference being the termination condition of the `binsearch` function. The first program terminates when `start` is greater than `end`, while the second program terminates when `start` equals `end`. The second approach is slightly more intuitive, as it reflects the fact that we have narrowed down the search range to a single element. However, the first approach is more efficient, as it minimizes the number of times the `binsearch` function is called.