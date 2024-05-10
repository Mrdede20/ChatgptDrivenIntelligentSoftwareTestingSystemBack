Sure, here are the two implementations for finding the kth-lowest element in a list using the QuickSelect algorithm: 

Implementation 1:

```
def quick_select(nums, k):
    pivot = nums[0]
    below = [num for num in nums if num < pivot]
    above = [num for num in nums if num > pivot]
    equal = [num for num in nums if num == pivot]
    
    if k < len(below):
        return quick_select(below, k)
    elif k < len(below) + len(equal):
        return pivot
    else:
        return quick_select(above, k - len(below) - len(equal))
```

Implementation 2:

```
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
```

Both of these implementations have the same method name and parameter type. In the first implementation, the pivot element is always the first element in the list. In the second implementation, a random element in the list is chosen as the pivot to reduce the chance of worst-case performance. The rest of the code is the same as described in the problem statement.