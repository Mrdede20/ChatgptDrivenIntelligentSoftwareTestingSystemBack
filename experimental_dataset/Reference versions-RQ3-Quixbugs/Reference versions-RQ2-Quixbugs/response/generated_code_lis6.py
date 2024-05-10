Program 1:

```
def lis(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
```

Program 2:

```
def lis(arr):
    n = len(arr)
    ends = {}
    longest = 0
    for i in range(n):
        ends[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                ends[i] = max(ends[i], ends[j]+1)
        longest = max(longest, ends[i])
    return longest
```

Both programs achieve the same intention of finding the length of the longest monotonically increasing subsequence in a given sequence of integers using dynamic programming approach. The first program achieves this using a list to store the length of the longest increasing subsequence upto index `i` and the second program stores the end of the sequence of a particular length in a dictionary.