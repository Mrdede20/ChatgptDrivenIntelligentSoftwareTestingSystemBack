Here are two different implementations of the same algorithm:

Implementation 1:

```
def max_subarray_sum(arr):
    max_so_far = max_ending_here = 0
    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

Implementation 2:

```
def max_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

Both implementations use the same approach of keeping track of the maximum sum seen so far and the maximum sum of the sublist ending at the current position. In implementation 1, both max_so_far and max_ending_here start at 0 and the loop starts iterating through the array from the beginning. In implementation 2, max_so_far and max_ending_here both start at the first element of the array and the loop starts iterating through the array from the second element.

Both implementations have a time complexity of O(n) and a space complexity of O(1).