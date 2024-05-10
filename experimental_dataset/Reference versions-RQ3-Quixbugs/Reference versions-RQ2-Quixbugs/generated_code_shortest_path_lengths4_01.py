
from collections import defaultdict

def shortest_path_lengths(n, length_by_edge):
    # Initialize all path lengths to infinity
    path_lengths = defaultdict(lambda: defaultdict(lambda: float('inf')))
    
    # Set diagonal path lengths to zero
    for i in range(n):
        path_lengths[i][i] = 0
    
    # Update path lengths using Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                path_lengths[i][j] = min(path_lengths[i][j], path_lengths[i][k] + path_lengths[k][j] + length_by_edge[i][j])
    
    # Return the shortest path lengths
    return dict(path_lengths)
