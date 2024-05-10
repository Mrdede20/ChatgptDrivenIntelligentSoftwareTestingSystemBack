Sure, here are two implementations of the "lis" function in Python:

Implementation 1:

```
def lis(arr):
    ends = {}
    longest = 0
    for num in arr:
        if not ends:
            ends[1] = num
            longest = 1
        else:
            left, right = 1, longest
            while left <= right:
                mid = (left + right) // 2
                if ends[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            ends[left] = num
            longest = max(longest, left)
    return longest
```

Implementation 2:

```
def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
```

Both implementations take a list of unique integers as input and return the length of the longest monotonically increasing subsequence of the list using dynamic programming. The first implementation uses binary search to find where to add the new elements to the "ends" dictionary, while the second implementation uses a nested loop to compare each element to previous ones and update the "dp" list accordingly. Both implementations have an O(n*logn) time complexity.