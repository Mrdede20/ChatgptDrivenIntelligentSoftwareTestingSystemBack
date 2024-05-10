
import numpy as np
from collections import defaultdict

def floyd_warshall(num_nodes, edges):
    # initialize distance matrix
    dist = np.full((num_nodes, num_nodes), np.inf)
    for n in range(num_nodes):
        dist[n, n] = 0
    # update distance matrix
    for u, v in edges:
        dist[u, v] = edges[(u, v)]
    # calculate shortest distances
    for k in range(num_nodes):
        dist = np.minimum(dist, np.add.outer(dist[:, k], dist[k, :]))
    # convert distance matrix to dictionary
    dist_dict = defaultdict(lambda: np.inf)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if dist[i, j] < np.inf:
                dist_dict[(i, j)] = dist[i, j]
    # return shortest distances
    return dist_dict
