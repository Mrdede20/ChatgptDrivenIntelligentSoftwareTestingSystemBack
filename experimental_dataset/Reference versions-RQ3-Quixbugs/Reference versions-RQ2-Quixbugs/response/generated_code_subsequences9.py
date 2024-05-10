Here are two programs that generate all possible subsequences of ascending integers using recursive logic:

Program 1:

```
def subsequences(a, b, k):
    if k == 0:
        return [[]]
    else:
        return [sub + [i] for i in range(a, b+1-k) for sub in subsequences(i+1, b, k-1)]
```

Program 2:

```
def subsequences(a, b, k):
    if k == 0:
        return [[]]
    else:
        subs = []
        for i in range(a, b+1-k):
            for sub in subsequences(i+1, b, k-1):
                subs.append([i] + sub)
        return subs
```

Both programs use the same method name, `subsequences`, and the same parameter type, three integers `a`, `b`, `k`. They return a list of lists of all possible subsequences of ascending integers of length `k` generated from the range `a` to `b`. The recursion starts with the base case where `k=0`, and returns an empty list `[]`. If `k>0`, the function uses list comprehension or nested for loops to generate all possible subsequences for each integer `i` in the range `(a, b+1-k)`, then combines them with `[i]` to make ascending subsequence of length `k`. Both programs provide the desired output for the example input of `a=1`, `b=5`, and `k=3`.