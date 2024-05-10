
from collections import defaultdict

def floyd_warshall(num_nodes, edges):
    shortest_paths = defaultdict(lambda: float('inf'))

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                shortest_paths[(i, j)] = 0
            elif (i, j) in edges:
                shortest_paths[(i, j)] = edges[(i, j)]

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                shortest_paths[(i, j)] = min(shortest_paths[(i, j)], shortest_paths[(i, k)] + shortest_paths[(k, j)])
       
    return shortest_paths
