Here are two programs that implement the binary search algorithm as described:

Program 1:

```
def binsearch(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binsearch(arr, left, mid-1, x)
        else:
            return binsearch(arr, mid+1, right, x)
    else:
        return -1

def find_in_sorted(arr, x):
    return binsearch(arr, 0, len(arr)-1, x)

# Example usage:
arr = [3, 4, 5, 5, 5, 5, 6]
x = 5
print(find_in_sorted(arr, x)) # output: 3
```

Program 2:

```
def binsearch(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def find_in_sorted(arr, x):
    return binsearch(arr, 0, len(arr)-1, x)

# Example usage:
arr = [3, 4, 5, 5, 5, 5, 6]
x = 5
print(find_in_sorted(arr, x)) # output: 3
```

Both programs use the same method name `binsearch` and the same parameter type of `arr`, `left`, `right`, and `x`. The first program uses recursion while the second program uses a while loop to implement the binary search algorithm. Both programs return the same output for the given example.