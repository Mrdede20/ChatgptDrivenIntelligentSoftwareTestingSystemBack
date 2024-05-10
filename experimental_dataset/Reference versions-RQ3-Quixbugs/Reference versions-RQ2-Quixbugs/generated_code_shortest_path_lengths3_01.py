
from collections import defaultdict

def floyd_warshall(num_nodes, edges):
    # Initialize distance dictionary
    dist = defaultdict(lambda: float('inf'))
    for i in range(num_nodes):
        dist[(i, i)] = 0
    
    # Update distance dictionary
    for u, v in edges:
        dist[(u, v)] = edges[(u, v)]
    
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[(i, j)] = min(dist[(i, j)], dist[(i, k)] + dist[(k, j)])
    
    return dict(dist)
