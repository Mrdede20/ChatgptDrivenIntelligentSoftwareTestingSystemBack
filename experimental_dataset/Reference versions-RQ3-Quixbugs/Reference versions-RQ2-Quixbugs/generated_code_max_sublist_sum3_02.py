
def max_sublist_sum(nums):
    if len(nums) == 0:
        return 0
    
    max_ending_here = nums[0]
    max_so_far = nums[0]
    
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
