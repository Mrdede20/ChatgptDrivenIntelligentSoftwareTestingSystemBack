
def find_maximum_subset(A, c, d):
    n = len(A)
    A.sort(reverse=True)
    total_sum = sum(A[:d])
    if total_sum >= c:
        return float("inf")
    if A[0] * d < c:
        return "impossible"
    left, right = 1, d
    while left <= right:
        mid = (left+right) // 2
        temp_sum = sum(A[:mid])
        repeats = (c-total_sum+temp_sum-1) // temp_sum
        if d-mid+1 >= repeats:
            return repeats+mid-1
        else:
            right = mid-1
    return "impossible"
