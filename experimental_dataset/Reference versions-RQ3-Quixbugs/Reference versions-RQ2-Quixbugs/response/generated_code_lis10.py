Option 1:

```python
def lis(arr):
    ends = {}
    for i in range(len(arr)):
        ends[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                ends[i] = max(ends[i], ends[j] + 1)
    return max(ends.values())
```
Option 2:

```python
def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

Both options implement the same functionality of finding the length of the longest monotonically increasing subsequence of a given sequence of integers using the dynamic programming approach. The first option uses a dictionary to store the lengths of the increasing subsequences that end at each position, while the second option uses a list to store the length of the longest increasing subsequence ending at each position. Both options have a time complexity of O(n^2) and a space complexity of O(n).