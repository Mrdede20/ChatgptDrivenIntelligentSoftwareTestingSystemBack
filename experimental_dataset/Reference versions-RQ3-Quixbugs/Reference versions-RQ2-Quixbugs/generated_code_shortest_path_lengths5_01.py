
from collections import defaultdict
from typing import Dict, Tuple

def floyd_warshall(n: int, length_by_edge: Dict[Tuple[int, int], int]) -> Dict[Tuple[int, int], int]:
    dist = defaultdict(lambda: float('inf'))
    for i in range(n):
        dist[(i, i)] = 0

    for key, value in length_by_edge.items():
        dist[key] = value

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[(i, j)] = min(dist[(i, j)], dist[(i, k)] + dist[(k, j)])

    return dict(dist)
