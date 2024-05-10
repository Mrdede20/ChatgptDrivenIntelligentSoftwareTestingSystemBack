Here are two implementations for the given intention:

Implementation 1:
```
def max_subarray_sum(arr):
    n = len(arr)
    max_ending_here = max_so_far = arr[0]
    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

Implementation 2:
```
def max_subarray_sum(arr):
    n = len(arr)
    max_sum = arr[0]
    temp_sum = arr[0]
    for i in range(1, n):
        temp_sum = max(arr[i], temp_sum+arr[i])
        max_sum = max(temp_sum, max_sum)
    return max_sum
```

Both implementations use dynamic programming approach to solve the problem in linear time complexity O(n). They keep track of the maximum sum ending at each element in the array and return the maximum sum among them.