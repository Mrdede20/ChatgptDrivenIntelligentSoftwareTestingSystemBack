
from collections import defaultdict

def floyd_warshall(num_nodes, edges):
    shortest_paths = defaultdict(lambda: float('inf'))

    for i in range(1, num_nodes+1):
        shortest_paths[(i,i)] = 0

    for edge, weight in edges.items():
        shortest_paths[edge] = weight

    for k in range(1, num_nodes+1):
        for i in range(1, num_nodes+1):
            for j in range(1, num_nodes+1):
                shortest_paths[(i,j)] = min(shortest_paths[(i,j)], shortest_paths[(i,k)]+shortest_paths[(k,j)])

    return shortest_paths
