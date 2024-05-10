Sure, here are two implementations of the Longest Increasing Subsequence (LIS) algorithm in Python:

Implementation 1:

```python
def find_lis(seq):
    n = len(seq)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis, default=0)
```

Implementation 2:

```python
def find_lis(seq):
    tails = [0] * len(seq)
    size = 0
    for x in seq:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size
```

Both implementations take a sequence of integers as input and return the length of the longest increasing subsequence in that sequence. The first implementation uses dynamic programming to keep track of the longest increasing subsequence seen so far for each index in the sequence. The second implementation uses a binary search algorithm to find the longest increasing subsequence ending at each index in the sequence.