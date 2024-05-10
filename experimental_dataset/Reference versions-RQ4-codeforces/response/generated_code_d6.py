Here are two programs, one using a brute force approach and the other using a more optimized approach:

Brute Force Approach:

```python
def solve(L):
    n = len(L)
    for i in range(n):
        temp = L[:i] + L[i+1:]
        flag = True
        for j in range(len(temp)-1):
            if temp[j] <= temp[j+1]:
                flag = False
                break
        if flag:
            return "YES"
    return "NO"
```

Optimized Approach:

```python
def solve(L):
    n = len(L)
    count = 0
    last = -1
    for i in range(n-1):
        if L[i] > L[i+1]:
            count += 1
            last = i
        if count > 1:
            return "NO"
    if count == 0:
        return "NO"
    if count == 1 and (last == 0 or last == n-2 or L[last-1] > L[last+1] or L[last] > L[last+2]):
        return "YES"
    else:
        return "NO"
```

Both programs take in a list of positive integers `L` and return either `YES` or `NO` depending on whether one element can be removed to make the list strictly decreasing. The optimized approach runs in O(n) time complexity, which makes it more efficient than the brute force approach that runs in O(n^2) time complexity.