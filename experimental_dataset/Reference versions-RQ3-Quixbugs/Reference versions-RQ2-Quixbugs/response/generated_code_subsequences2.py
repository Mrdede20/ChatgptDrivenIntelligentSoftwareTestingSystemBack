Program 1:

```
def allSubsequences(a, b, k):
    if k == 0:
        return []
    
    if k == 1:
        return [[i] for i in range(a, b+1)]
    
    res = []
    for i in range(a, b+1):
        subseqs = allSubsequences(i+1, b, k-1)
        for sub in subseqs:
            res.append([i] + sub)
    
    return res
```

Program 2:

```
def allSubsequences(a, b, k):
    if k == 0:
        return []
    
    res = []
    for i in range(a, b+1):
        if k == 1:
            res.append([i])
        else:
            subseqs = allSubsequences(i+1, b, k-1)
            for sub in subseqs:
                res.append([i] + sub)
    
    return res
```

Both of these programs use recursion and backtracking to generate a list of all possible length-k ascending subsequences of integers in the range from "a" to "b" inclusively. The difference between them is in the order of checking the value of the "k" parameter. Program 1 checks if k=1 first and generates a subsequence for each element in the range, while Program 2 generates subsequences for each element in the range and appends the element at the end if k=1.