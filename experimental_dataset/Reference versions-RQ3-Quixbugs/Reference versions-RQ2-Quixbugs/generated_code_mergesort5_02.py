
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
