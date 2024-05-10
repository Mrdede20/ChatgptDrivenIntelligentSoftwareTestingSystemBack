Sure, here are two example programs:

#### Program 1
```python
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
```

#### Program 2
```python
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
```

Both of these programs use the same method name (`max_sublist_sum`) and parameter type (`List[int]`). They also use dynamic programming to efficiently find the maximum contiguous sublist sum of a given list of integers. The `max_sublist_sum` function takes in a list of integers, finds the maximum sum of all the contiguous sublists within the list, and returns that maximum sum. 

I hope this helps!