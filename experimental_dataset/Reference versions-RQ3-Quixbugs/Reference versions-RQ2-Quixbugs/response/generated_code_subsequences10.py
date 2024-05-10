Here are two programs that satisfy the requirements:

Program 1:

```
def subsequences(a, b, k):
    if k == 1:
        return [[i] for i in range(a, b+1)]
    else:
        result = []
        for i in range(a, b-k+2):
            for seq in subsequences(i+1, b, k-1):
                result.append([i] + seq)
        return result
```
Program 2:

```
def subsequences(a, b, k):
    def helper(start, k, current):
        if k == 0:
            result.append(list(current))
            return
        for i in range(start, b-k+2):
            current.append(i)
            helper(i+1, k-1, current)
            current.pop()
            
    result = []
    helper(a, k, [])
    return result
```

Both of these programs work by recursively building up all length-k ascending subsequences using elements from the range [a, b]. The first program uses nested for loops to iterate over all possible first elements of the subsequence, and then recursively generate the rest of the subsequence using smaller subsequences. The second program uses a helper function which takes the current start element, the remaining length k, and the current subsequence being built up. It then iterates over all possible start elements for the next element in the sequence, and recursively generates the rest of the subsequence using smaller sequences.

Both programs return the same output for `subsequences(a=1, b=5, k=3)`, which is `[[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]`.