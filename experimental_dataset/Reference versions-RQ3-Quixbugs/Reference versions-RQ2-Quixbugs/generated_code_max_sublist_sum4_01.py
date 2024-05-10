
def max_sublist_sum(nums):
    """
    Finds the maximum contiguous sublist sum of a given list of integers using dynamic programming.

    Args:
        nums (List[int]): A list of integers

    Returns:
        int: The maximum contiguous sublist sum

    Example:
        >>> max_sublist_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
    """
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum
