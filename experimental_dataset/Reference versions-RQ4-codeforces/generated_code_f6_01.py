
def calculate_k(t:int, queries:List[Tuple[int,int,int,List[int]]]) -> List[int]:
    results = []
    for i in range(t):
        n, c, d, A = queries[i]
        A.sort(reverse=True)
        if sum(A[:d]) >= c:
            results.append("Infinity")
        elif sum(A[:d]) * d < c:
            results.append("Impossible")
        else:
            left = 0
            right = n // (d+1) + 1
            while left < right:
                mid = (left+right) // 2
                selected_sum = 0
                j = 0
                k = mid * (d+1)
                while j < d and k > 0:
                    selected_sum += A[j]
                    j += 1
                    k -= 1
                while k > 0:
                    selected_sum += A[j]
                    j += 1
                    k -= mid
                if selected_sum >= c:
                    right = mid
                else:
                    left = mid + 1
            results.append(left)
    return results
