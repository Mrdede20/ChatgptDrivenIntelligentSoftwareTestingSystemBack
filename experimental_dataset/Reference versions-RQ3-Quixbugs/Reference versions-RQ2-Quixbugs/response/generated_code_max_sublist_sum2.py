Here's a Python program that uses Kadane's algorithm to find the maximum sum of a subarray in a given list of integers:

```python
def max_sublist_sum(lst):
    # Initialize variables
    max_sum = lst[0]
    curr_sum = lst[0]

    # Iterate through list
    for num in lst[1:]:
        # Calculate current sum
        curr_sum = max(num, curr_sum + num)

        # Update max sum
        max_sum = max(max_sum, curr_sum)

    return max_sum
```

Here's a second version of the function that uses a slightly different approach:

```python
def max_sublist_sum(lst):
    # Initialize variables
    max_sum = 0
    curr_sum = 0

    # Iterate through list
    for num in lst:
        # Calculate current sum
        curr_sum = max(0, curr_sum + num)

        # Update max sum
        max_sum = max(max_sum, curr_sum)

    return max_sum
```

Both versions of the program take a list of integers as input and use Kadane's algorithm to find the maximum sum of a subarray. The first version initializes the maximum and current sums to the first element of the list, then iterates through the remaining elements and updates the current sum and maximum sum as needed. The second version initializes both sums to 0 and uses the maximum of the current sum and 0 as the new value for the current sum at each step. The maximum sum is updated accordingly.