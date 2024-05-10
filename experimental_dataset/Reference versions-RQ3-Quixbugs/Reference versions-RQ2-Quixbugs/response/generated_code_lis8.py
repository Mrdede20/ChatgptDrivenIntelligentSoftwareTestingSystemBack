Sure, here are two programs that implement the Longest Increasing Subsequence problem in Python using the same method name and parameter type:

Program 1:

```python
def longest_increasing_subsequence(sequence):
    ends = {}
    longest = 0

    for num in sequence:
        i, j = 0, longest
        while i != j:
            mid = (i + j) // 2
            if ends[mid] < num:
                i = mid + 1
            else:
                j = mid
        ends[i] = num
        longest = max(longest, i+1)

    return longest
```

Program 2:
```python
def longest_increasing_subsequence(sequence):
    dp = [1] * len(sequence)

    for i in range(len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)
```

Both programs use different algorithms to solve the Longest Increasing Subsequence problem in Python. Program 1 uses a binary search algorithm to find the end of each increasing subsequence, while Program 2 uses a dynamic programming approach to solve the problem.