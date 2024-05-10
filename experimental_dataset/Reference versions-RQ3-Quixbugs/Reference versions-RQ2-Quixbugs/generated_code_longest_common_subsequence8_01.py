
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
