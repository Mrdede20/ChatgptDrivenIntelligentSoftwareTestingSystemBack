Sure, here are two solutions:

Solution 1:
```
def max_sublist_sum(arr):
    if not arr:
        return 0

    max_ending_here = arr[0]
    max_so_far = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```

Solution 2:
```
def max_sublist_sum(arr):
    if not arr:
        return 0

    max_ending_here = 0
    max_so_far = float('-inf')

    for num in arr:
        max_ending_here += num
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(0, max_ending_here)

    return max_so_far if max_so_far != float('-inf') else 0
```

Both of these solutions implement the same algorithm and have the same time complexity of O(n). The only difference is in how they initialize and update the `max_ending_here` and `max_so_far` variables. Solution 1 initializes both variables to the first element in the list and updates them based on the current element. Solution 2 initializes `max_ending_here` to zero and `max_so_far` to negative infinity, and updates them based on the current element.