
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
