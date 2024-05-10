
import random

def quick_select(nums, k):
    if len(nums) == 1:
        return nums[0]
    
    pivot = random.choice(nums)
    below = [num for num in nums if num < pivot]
    above = [num for num in nums if num > pivot]
    equal = [num for num in nums if num == pivot]
    
    if k < len(below):
        return quick_select(below, k)
    elif k < len(below) + len(equal):
        return pivot
    else:
        return quick_select(above, k - len(below) - len(equal))
