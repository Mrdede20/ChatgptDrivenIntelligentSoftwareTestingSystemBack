
def next_permutation(nums):
    """
    This function takes a list of unique integers and returns the lexicographically next permutation of the elements
    of the list. If no such permutation exists, it returns None.
    """
    n = len(nums)
    i = n - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:
        return None
    j = n - 1
    while j >= i and nums[j] <= nums[i-1]:
        j -= 1
    nums[i-1], nums[j] = nums[j], nums[i-1]
    nums[i:] = reversed(nums[i:])
    return nums
