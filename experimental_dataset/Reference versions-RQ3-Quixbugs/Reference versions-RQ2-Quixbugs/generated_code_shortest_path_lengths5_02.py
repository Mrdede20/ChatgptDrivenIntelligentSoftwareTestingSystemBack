
from collections import defaultdict
from typing import Dict, Tuple

def floyd_warshall(n: int, length_by_edge: Dict[Tuple[int, int], int]) -> Dict[Tuple[int, int], int]:
    dist = defaultdict(lambda: float('inf'))
    for i in range(n):
        dist[(i, i)] = 0

    for key in length_by_edge:
        dist[key] = length_by_edge[key]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[(i, k)] + dist[(k, j)] < dist[(i, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]

    return dict(dist)
