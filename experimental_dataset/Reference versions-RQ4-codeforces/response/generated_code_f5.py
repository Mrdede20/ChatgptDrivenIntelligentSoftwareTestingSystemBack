Sure, here are two possible implementations of the program:

Implementation 1:

```
def find_elements(A, c, n, d):
    A.sort()
    start, end = d-1, n-1
    while start <= end:
        mid = (start+end)//2
        if sum(A[mid-d+1:mid+1]) <= c:
            start = mid+1
        else:
            end = mid-1
    if start == n:
        return "Infinity"
    elif sum(A[start-d:start]) >= c:
        return start-d+1
    else:
        return "Impossible"
```

Implementation 2:

```
def find_elements(A, c, n, d):
    A.sort()
    left, right = d-1, n-1
    res = n+1
    while left <= right:
        mid = (left + right)//2
        if A[mid] > c:
            right = mid-1
        else:
            temp_res = [0]*(d-1) + [1]*(mid-d+2) #initialize as d-1 zeroes and mid-d+2 ones
            i, j = mid-d+1, d-2 # initialize two pointers
            while i >= 0 and j >= 0:
                if A[i] + temp_res[j] <= c:
                    temp_res[j] += A[i]
                    i -= 1
                    j -= 1
                else:
                    i -= 1
            if j == -1: #we were able to find d elements
                res = min(res, mid)
                right = mid-1
            else:
                left = mid+1
    if res == n+1:
        return "Impossible"
    elif sum(A[res-d+1:res+1]) >= c:
        return res-d+1
    else:
        return "Infinity"
```

Both implementations take in the same input arguments: a list A of integers, a target integer c, and two integers n and d.

The first implementation uses binary search to find the maximum number of elements that can be selected from the list without making the sum exceed c, while also satisfying the constraint that a certain number (d) of elements must be selected. It returns either the maximum number of elements that can be selected or "Infinity" if the selection sum is already greater than or equal to c, or "Impossible" if it is not possible to select enough elements to make the sum greater than or equal to c.

The second implementation also uses binary search to find the maximum number of elements that can be selected from the list without making the sum exceed c, while also satisfying the constraint that a certain number (d) of elements must be selected. It uses a slightly different logic to find these elements, by initializing a list of size d-1 with zeroes and mid-d+2 with ones, and then iterating over the sublist of A from 0 to mid, adding the largest elements to the ones in the initialized list, until we have d elements that add up to at least c. If this is not possible, we continue the binary search. This implementation also returns either the maximum number of elements that can be selected or "Infinity" if the selection sum is already greater than or equal to c, or "Impossible" if it is not possible to select enough elements to make the sum greater than or equal to c.