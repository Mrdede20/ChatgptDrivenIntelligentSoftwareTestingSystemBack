Here's the first solution using dynamic programming with a 2D dictionary:

```python
def lcs_length(s: str, t: str) -> int:
    dp = {}
    max_len = 0
    for i in range(len(s)):
        for j in range(len(t)):
            if i == 0 or j == 0:
                dp[(i,j)] = 0
            elif s[i-1] == t[j-1]:
                dp[(i,j)] = dp[(i-1, j-1)] + 1
                max_len = max(max_len, dp[(i,j)])
            else:
                dp[(i,j)] = 0
    return max_len
```

Here's another solution that uses nested loops to iterate through all possible substrings of the two input strings and return the length of the longest common substring:

```python
def lcs_length(s: str, t: str) -> int:
    max_len = 0
    for i in range(len(s)):
        for j in range(len(t)):
            k = 0
            while i + k < len(s) and j + k < len(t) and s[i+k] == t[j+k]:
                k += 1
            if k > max_len:
                max_len = k
    return max_len
```

Both solutions have the same method name and parameter types, and they achieve the intended purpose of finding the length of the longest common substring between two input strings `s` and `t`.