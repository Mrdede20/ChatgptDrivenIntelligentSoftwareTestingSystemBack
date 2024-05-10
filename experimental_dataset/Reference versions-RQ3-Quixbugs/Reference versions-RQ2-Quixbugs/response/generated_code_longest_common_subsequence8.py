Here are two Python programs that achieve the same intention of finding the longest common subsequence between two given strings using a recursive approach. Both programs use the same method name and parameter type.

Program 1: Using Memoization

```
def find_lcs(a, b):
    memo = {}
    
    def recurse(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(a) or j == len(b):
            result = ""
        elif a[i] == b[j]:
            result = a[i] + recurse(i+1, j+1)
        else:
            sub1 = recurse(i+1, j)
            sub2 = recurse(i, j+1)
            sub3 = recurse(i+1, j+1)
            result = max(sub1, sub2, sub3, key=len)
        
        memo[(i, j)] = result
        return result
    
    return recurse(0, 0)
```

Explanation: This program uses memoization to avoid recalculating already seen subproblems. It creates a memo dictionary to store the results of subproblems already computed. The base cases and recursive cases are the same as described in the intention. The only difference is that the function checks the memo dictionary for entries first, and returns them if they exist, rather than recalculating them.

Program 2: Using Recursive Function

```
def find_lcs(a, b):
    
    def recurse(i, j):
        if i == len(a) or j == len(b):
            result = ""
        elif a[i] == b[j]:
            result = a[i] + recurse(i+1, j+1)
        else:
            sub1 = recurse(i+1, j)
            sub2 = recurse(i, j+1)
            sub3 = recurse(i+1, j+1)
            result = max(sub1, sub2, sub3, key=len)
        
        return result
    
    return recurse(0, 0)
```

Explanation: This program does not use memoization and instead relies on recursion to find the longest common subsequence. It follows the same logic as the previous program, with the base cases and recursive cases being the same. However, it does not store already computed results, which can lead to redundant calculations for the same subproblem. This program is provided for comparison and reference purposes.