
from collections import defaultdict

def floyd_warshall(num_nodes, edges):
    # initialize distance dictionary
    dist = defaultdict(lambda: float('inf'))
    for n in range(num_nodes):
        dist[(n, n)] = 0
    # update distance dictionary
    for u, v in edges:
        dist[(u, v)] = edges[(u, v)]
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[(i, j)] = min(dist[(i, j)], dist[(i, k)] + dist[(k, j)])
    # return shortest distances
    return dist
