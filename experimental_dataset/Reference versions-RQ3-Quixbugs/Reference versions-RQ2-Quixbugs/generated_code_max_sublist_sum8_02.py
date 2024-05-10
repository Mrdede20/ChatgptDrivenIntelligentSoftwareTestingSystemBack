
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
