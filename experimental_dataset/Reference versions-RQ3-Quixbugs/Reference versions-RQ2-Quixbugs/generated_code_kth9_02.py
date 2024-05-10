
def QuickSelect(nums, k):
    pivot = nums[0]
    less_nums = [num for num in nums if num < pivot]
    equal_nums = [num for num in nums if num == pivot]
    num_less = len(less_nums)
    num_equal = len(equal_nums)
    num_greatereq = len(nums) - num_less - num_equal
    
    if k < num_less:
        return QuickSelect(less_nums, k)
    elif k >= num_less + num_equal:
        return QuickSelect([num for num in nums if num > pivot], k - num_less - num_equal)
    else:
        return pivot
