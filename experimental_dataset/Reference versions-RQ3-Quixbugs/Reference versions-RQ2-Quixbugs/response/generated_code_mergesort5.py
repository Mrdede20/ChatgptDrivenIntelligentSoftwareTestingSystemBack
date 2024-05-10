Sure, here are two Python programs that achieve the same intention using the merge sort algorithm:

Program 1:
```python
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
```

Program 2:
```python
def mergesort(nums):
    if len(nums) > 1:
        # split the list into two halves
        mid = len(nums)//2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # recursively sort the two halves
        mergesort(left_half)
        mergesort(right_half)

        # merge the sorted halves
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        # check if any elements are left in either half
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1
```
Both the programs take a list of integers as input parameter and return a sorted list using the merge sort algorithm.