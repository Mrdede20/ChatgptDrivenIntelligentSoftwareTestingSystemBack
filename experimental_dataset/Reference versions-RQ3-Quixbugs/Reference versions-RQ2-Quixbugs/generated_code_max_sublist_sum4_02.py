
def max_sublist_sum(nums):
    """
    Finds the maximum contiguous sublist sum of a given list of integers using dynamic programming.

    Args:
        nums (List[int]): A list of integers

    Returns:
        int: The maximum contiguous sublist sum

    Example:
        >>> max_sublist_sum([1, -2, 3, 4, -5, 8])
        10
    """
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0
        
    return max_sum
