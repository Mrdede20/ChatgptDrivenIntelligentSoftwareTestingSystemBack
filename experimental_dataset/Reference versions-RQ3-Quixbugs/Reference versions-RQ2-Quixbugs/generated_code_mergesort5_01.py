
def mergesort(nums):
    # base case: list is already sorted if it is empty or has only one element
    if len(nums) <= 1:
        return nums
    
    # divide the list into two halves
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]
    
    # recursively sort the two halves
    left_half = mergesort(left_half)
    right_half = mergesort(right_half)
    
    # merge the sorted halves
    sorted_nums = merge(left_half, right_half)
    return sorted_nums

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
