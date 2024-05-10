Program 1:

```python
def longest_increasing_subsequence(arr):
    ends = {}
    longest = 0
    for num in arr:
        l, r = 0, longest
        while l < r:
            mid = (l + r) // 2
            if ends[mid] < num:
                l = mid + 1
            else:
                r = mid
        ends[l] = num
        longest = max(longest, l + 1)
    return longest
```

Program 2:

```python
def longest_increasing_subsequence(arr):
    ends = []
    for num in arr:
        l, r = 0, len(ends)
        while l < r:
            mid = (l + r) // 2
            if ends[mid] < num:
                l = mid + 1
            else:
                r = mid
        if l == len(ends):
            ends.append(num)
        else:
            ends[l] = num
    return len(ends)
```

Both programs implement the same dynamic programming approach known as the "Patience Sorting Algorithm". The first program uses a dictionary to store the last element of each subsequence, while the second program uses a list.

The main difference between the two programs is how they handle the case when a new subsequence needs to be started. In the first program, the length of the longest subsequence is increased by 1. In the second program, a new element is appended to the "ends" list if it can't be added to an existing subsequence.

Both programs have a time complexity of O(n log n), where n is the length of the input array.