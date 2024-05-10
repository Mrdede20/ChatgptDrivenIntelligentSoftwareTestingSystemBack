Here are two Python programs that solve the problem of finding the length of the longest monotonically increasing subsequence of a given sequence of integers. They both use the same method name 'lis' and the same parameter type of an array.

Program 1:

```
def lis(arr):
    ends = {}
    for i in range(len(arr)):
        ends[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                ends[i] = max(ends[i], ends[j] + 1)
    return max(ends.values())
```

Program 2:

```
def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

Both programs have the same time complexity of O(n^2) and the same space complexity of O(n). Program 1 uses a dictionary to keep track of the ends of the longest increasing subsequence of various lengths, while Program 2 uses a list to keep track of the length of the longest increasing subsequence ending at each index.