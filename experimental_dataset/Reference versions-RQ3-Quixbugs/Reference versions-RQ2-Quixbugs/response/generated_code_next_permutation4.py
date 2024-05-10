Here are two implementations of the "Next Permutation" algorithm in Python:

Implementation 1:

```python
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
```

Implementation 2:

```python
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
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
    # Step 4: Reverse the remaining portion of the list
    start = i + 1
    end = len(nums) - 1
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1
    
    return nums
```

Both implementations use the same method name `next_permutation` and the same parameter type `nums`, which is a list of integers. The first implementation uses the `reversed` function to reverse the remaining portion of the list, while the second implementation uses a while loop to perform the same task.