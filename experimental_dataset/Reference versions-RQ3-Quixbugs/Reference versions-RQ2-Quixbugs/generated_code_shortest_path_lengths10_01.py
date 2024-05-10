
from collections import defaultdict

def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    
    # Initialize diagonal elements as 0
    for i in range(n):
        length_by_path[i, i] = 0
    
    # Update length_by_path with provided edges
    for (u, v), length in length_by_edge.items():
        length_by_path[u, v] = length
    
    # Evaluate shortest path length between all pairs of nodes
    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(length_by_path[i, j], length_by_path[i, k] + length_by_path[k, j])
    
    return dict(length_by_path)
