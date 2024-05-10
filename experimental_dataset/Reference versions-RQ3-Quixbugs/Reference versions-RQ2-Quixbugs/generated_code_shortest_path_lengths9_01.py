
from collections import defaultdict

def floyd_warshal(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    for i in range(n):
        length_by_path[(i, i)] = 0
    for u, v in length_by_edge.keys():
        length_by_path[(u, v)] = length_by_edge[(u, v)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[(i, j)] = min(length_by_path[(i, j)], length_by_path[(i, k)] + length_by_path[(k, j)])
    return dict(length_by_path)
