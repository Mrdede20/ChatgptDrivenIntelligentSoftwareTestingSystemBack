
from collections import defaultdict

def floyd_warshall(num_nodes, edges):
    # create a defaultdict with infinity as default value
    path_lengths = defaultdict(lambda: float('inf'))
    
    # set the length of the shortest path between each node and itself as 0
    for i in range(num_nodes):
        path_lengths[(i, i)] = 0
    
    # set the length of paths between nodes as given in the input dictionary
    for edge, dist in edges.items():
        path_lengths[edge] = dist
    
    # compute shortest path lengths through all possible intermediate nodes
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                path_lengths[(i, j)] = min(path_lengths[(i, j)], path_lengths[(i, k)] + path_lengths[(k, j)])
    
    return path_lengths
