Here's one implementation of the `max_sublist_sum` function using the above-described algorithm:

```
def max_sublist_sum(nums):
    max_so_far = 0
    max_ending_here = 0
    
    for num in nums:
        max_ending_here += num
        if max_ending_here < 0:
            max_ending_here = 0
        
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
```

Here's another implementation of `max_sublist_sum` using dynamic programming:

```
def max_sublist_sum(nums):
    if len(nums) == 0:
        return 0
    
    max_ending_here = nums[0]
    max_so_far = nums[0]
    
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
```

Both implementations have the same function signature of `max_sublist_sum(nums)`, where `nums` is a list of integers.