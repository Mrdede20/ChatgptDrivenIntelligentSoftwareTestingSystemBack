
def maximum_sublist_sum(nums):
    """
    Find the maximum sum of any consecutive subarray within a given list of integers using dynamic programming.

    Args:
    - nums: a list of integers

    Returns:
    - the maximum sum of any consecutive subarray
    """
    dp = [nums[0]] * len(nums)
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
    return max(dp)
