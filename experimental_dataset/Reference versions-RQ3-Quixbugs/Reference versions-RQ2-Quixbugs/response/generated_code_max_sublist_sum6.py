Sure, here are two programs that achieve the intention:

Program 1:

```
def max_sublist_sum(arr):
    """
    Finds the maximum sum of contiguous sublists in a given list of integers using Kadane's algorithm

    Example:
    max_sublist_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) returns 6

    :param arr: List of integers
    :return: Maximum sum of any contiguous sublist of the list
    """
 
    max_so_far = 0
    max_ending_here = 0
 
    for i in arr:
        max_ending_here = max_ending_here + i
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
 
    return max_so_far
```

Program 2:

```
def max_sublist_sum(arr):
    """
    Finds the maximum sum of contiguous sublists in a given list of integers using Kadane's algorithm

    Example:
    max_sublist_sum([4, -1, 2, 1]) returns 6

    :param arr: List of integers
    :return: Maximum sum of any contiguous sublist of the list
    """
 
    max_ending_here = max_so_far = arr[0]
 
    for i in arr[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```

Both of these programs implement Kadane's algorithm to find the maximum sum of contiguous sublists in a given integer array. Both programs take in a list of integers as input and return the maximum sum of any contiguous sublist of the list.