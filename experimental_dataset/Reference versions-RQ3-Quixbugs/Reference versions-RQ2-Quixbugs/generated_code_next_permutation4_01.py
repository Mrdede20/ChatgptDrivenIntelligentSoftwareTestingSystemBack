
def next_permutation(nums):
    # Step 1: Find the first element from the right that is less than its neighbor on the right
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
        
    if i == -1:
        return None
    
    # Step 2: Find the smallest element from the right that is greater than nums[i]
    j = len(nums) - 1
    while j >= i + 1 and nums[j] <= nums[i]:
        j -= 1
    
    # Step 3: Swap nums[i] and nums[j]
    nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the remaining portion of the list
    nums[i + 1:] = reversed(nums[i + 1:])
    
    return nums
