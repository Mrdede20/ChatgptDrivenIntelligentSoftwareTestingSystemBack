Program 1:

```python
def max_sublist_sum(lst):
    """
    Finds the maximum sum of any contiguous sublist in the input list of integers.
    
    Args:
    lst (list): Input list of integers
    
    Returns:
    int: Maximum sum of any contiguous sublist in the input list
      
    """
    max_ending_here = max_so_far = lst[0] # initialize both variables to the value of first element in the list
    
    for elem in lst[1:]:
        max_ending_here = max(elem, max_ending_here + elem) # update max_ending_here variable
        max_so_far = max(max_so_far, max_ending_here) # update max_so_far variable
        
    return max_so_far
```

Program 2:

```python
def max_sublist_sum(lst):
    """
    Finds the maximum sum of any contiguous sublist in the input list of integers.
    
    Args:
    lst (list): Input list of integers
    
    Returns:
    int: Maximum sum of any contiguous sublist in the input list
      
    """
    max_ending_here = 0 # initialize both variables to zero
    max_so_far = 0 
    
    for elem in lst:
        max_ending_here = max(0, max_ending_here + elem) # update max_ending_here variable
        max_so_far = max(max_so_far, max_ending_here) # update max_so_far variable
        
    return max_so_far
```

Both programs follow the same algorithm of maintaining two variables `max_ending_here` and `max_so_far` while iterating through the input list. Program 1 initializes both variables to the first element of the list, whereas Program 2 initializes them to zero. This difference in initialization allows Program 2 to handle negative numbers in the input list, as the `max_ending_here` variable is reset to zero everytime it becomes negative.