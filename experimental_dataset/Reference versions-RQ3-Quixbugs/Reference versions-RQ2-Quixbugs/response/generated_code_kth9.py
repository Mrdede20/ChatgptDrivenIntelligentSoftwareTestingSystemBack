Program 1:

```
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
```

Program 2 (optimized version):

```
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
```

Note: The optimized version of QuickSelect algorithm breaks the input list into three sublists, one containing elements less than the pivot, the second containing elements equal to the pivot, and, the third containing elements greater than the pivot. This improves the algorithm's performance by reducing the number of recursion calls in some specific cases.
