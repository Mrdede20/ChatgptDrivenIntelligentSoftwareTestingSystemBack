Program 1:

```
def longest_common_substring(s, t):
    if not s or not t:
        return 0
    counter = [[0] * len(t) for _ in range(len(s))]
    max_length = 0
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    counter[i][j] = 1
                else:
                    counter[i][j] = counter[i-1][j-1] + 1
                max_length = max(max_length, counter[i][j])
    return max_length
```

Program 2:

```
def longest_common_substring(s, t):
    if not s or not t:
        return 0
    counter = [[0] * (len(t)+1) for _ in range(len(s)+1)]
    max_length = 0
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                counter[i][j] = counter[i-1][j-1] + 1
                max_length = max(max_length, counter[i][j])
    return max_length
```

The main difference between these two programs is the initialization of the 2D array (Counter). The first program initializes it with `[[0] * len(t) for _ in range(len(s))]`, while the second program initializes it with `[[0] * (len(t)+1) for _ in range(len(s)+1)]`. The second program adds an extra row and column to the 2D array and initializes them with zeros, which simplifies the logic in the rest of the program.