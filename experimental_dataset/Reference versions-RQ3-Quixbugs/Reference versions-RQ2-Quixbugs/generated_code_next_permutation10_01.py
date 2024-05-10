
def next_permutation(nums):
    """
    This function takes a list of unique integers and returns the lexicographically next permutation of the elements
    of the list. If no such permutation exists, it returns None.
    """
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = reversed(nums[i+1:])
    return nums if i >= 0 else None
