
def select_items(A, c, d):
    A.sort(reverse=True)
    sum_d = sum(A[:d])
    if sum_d >= c:
        return "Infinity"
    elif A[0] * d < c:
        return "Impossible"
    else:
        l = 1
        r = len(A)
        while l < r:
            mid = (l + r) // 2
            selected = []
            weight = 0
            for i in range(mid):
                selected.append(A[i])
                weight += A[i]
            if weight >= c:
                r = mid
            else:
                l = mid + 1
        return l
