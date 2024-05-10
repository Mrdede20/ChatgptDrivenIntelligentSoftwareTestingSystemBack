
def maximum_sublist_sum(nums):
    """
    Find the maximum sum of any consecutive subarray within a given list of integers using Kadane's algorithm.

    Args:
    - nums: a list of integers

    Returns:
    - the maximum sum of any consecutive subarray
    """
    max_so_far = max_ending_here = nums[0]
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
