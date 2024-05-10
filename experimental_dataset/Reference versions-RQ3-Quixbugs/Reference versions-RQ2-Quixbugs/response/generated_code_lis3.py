Program 1:
```
def longest_increasing_subsequence(seq):
    n = len(seq)
    ends = {}
    longest = 0
    for i in range(n):
        ends[i] = 1
        for j in range(i):
            if seq[j] < seq[i]:
                ends[i] = max(ends[i], ends[j]+1)
        longest = max(longest, ends[i])
    return longest
```

Program 2 (with memoization):
```
def longest_increasing_subsequence(seq, ends={}):
    n = len(seq)
    if n not in ends:
        ends[n] = 1
        for i in range(n-1, -1, -1):
            if seq[i] < seq[n-1]:
                ends[n] = max(ends[n], longest_increasing_subsequence(seq[:i+1], ends)+1)
    return ends[n]
``` 

Note: Both programs have the same function name and parameter type. The second program uses memoization to reduce redundant calculations by caching lengths of previously calculated subsequences in the dict "ends".