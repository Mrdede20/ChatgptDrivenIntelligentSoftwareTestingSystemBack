Program 1:

```python
def find_maximum_sublist_sum(lst):
    max_sum_ending_here = max_sum_so_far = lst[0]
    for num in lst[1:]:
        max_sum_ending_here = max(num, max_sum_ending_here + num)
        max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)
    return max_sum_so_far
```

Program 2:

```python
def find_maximum_sublist_sum(lst):
    max_sum_ending_here = max_sum_so_far = lst[0]
    for num in lst[1:]:
        if max_sum_ending_here < 0:
            max_sum_ending_here = num
        else:
            max_sum_ending_here += num
        if max_sum_ending_here > max_sum_so_far:
            max_sum_so_far = max_sum_ending_here
    return max_sum_so_far
```

Both programs have the same method name and parameter type, and use Kadane's algorithm to find the maximum sum of a sublist within a given list. The second program has an additional check for negative maximum sum ending at a position, as this could potentially decrease the maximum sum.