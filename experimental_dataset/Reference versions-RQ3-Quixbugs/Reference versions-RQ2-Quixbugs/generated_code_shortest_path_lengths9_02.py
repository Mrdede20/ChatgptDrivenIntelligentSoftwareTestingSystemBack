
from collections import defaultdict

def floyd_warshal(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    for u, v in length_by_edge.keys():
        length_by_path[(u, v)] = length_by_edge[(u, v)]
    for i in range(n):
        length_by_path[(i, i)] = 0
        for j in range(i+1, n):
            for k in range(i+1, j):
                if length_by_path[(i, j)] > length_by_path[(i, k)] + length_by_path[(k, j)]:
                    length_by_path[(i, j)] = length_by_path[(i, k)] + length_by_path[(k, j)]
                    length_by_path[(j, i)] = length_by_path[(i, j)]
    return dict(length_by_path)
