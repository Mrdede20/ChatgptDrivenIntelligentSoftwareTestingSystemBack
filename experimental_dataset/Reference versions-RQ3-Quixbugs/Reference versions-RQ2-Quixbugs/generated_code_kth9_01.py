
def QuickSelect(nums, k):
    pivot = nums[0]
    num_less = len([num for num in nums[1:] if num <= pivot])
    num_greatereq = len(nums) - num_less - 1
    
    if k < num_less:
        return QuickSelect([num for num in nums[1:] if num <= pivot], k)
    elif k >= num_less + 1:
        return QuickSelect([num for num in nums[1:] if num > pivot], k - num_less - 1)
    else:
        return pivot
