Here are two programs implementing the Next Permutation algorithm in Python:

Program 1:

```python
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
```

Program 2:

```python
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
```

Both programs have the same function name `next_permutation` and the same parameter type, i.e., a list of unique integers. The algorithm used here is the same, but the implementation is slightly different. Program 1 starts with i=n-2 and moves backwards, while Program 2 starts with i=n-1 and moves backwards. Both programs return the lexicographically next permutation of the input list. If there is no such permutation, None is returned.