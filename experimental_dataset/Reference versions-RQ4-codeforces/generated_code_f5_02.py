
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
