
from heapq import heappush, heappop

def calculate_k(t:int, queries:List[Tuple[int,int,int,List[int]]]) -> List[int]:
    results = []
    for i in range(t):
        n, c, d, A = queries[i]
        A = [-a for a in A]
        heapq.heapify(A)
        if -sum(heapq.nsmallest(d, A)) >= c:
            results.append("Infinity")
        elif -sum(heapq.nsmallest(d, A)) * d < c:
            results.append("Impossible")
        else:
            left = 0
            right = n // (d+1) + 1
            while left < right:
                mid = (left+right) // 2
                heap = []
                selected_sum = 0
                for j in range(d):
                    selected_sum -= heapq.heappushpop(A, 0)
                heappush(heap, selected_sum)
                for j in range(mid-1):
                    selected_sum = 0
                    for k in range(d+1):
                        if len(A) > 0:
                            selected_sum -= heapq.heappop(A)
                    heappush(heap, selected_sum)
                if -sum(heapq.nsmallest(d-1, heap)) >= c:
                    right = mid
                else:
                    left = mid + 1
            results.append(left)
    return results
