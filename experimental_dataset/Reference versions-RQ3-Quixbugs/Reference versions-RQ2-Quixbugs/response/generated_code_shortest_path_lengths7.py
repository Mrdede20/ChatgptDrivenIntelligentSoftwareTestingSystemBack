Sure, here are two programs implementing the Floyd-Warshall algorithm:

First program using nested loops:

```python
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
```

Second program using numpy to optimize nested loops:

```python
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
```

Both functions take in the same parameters and return the shortest distances between every ordered pair of nodes in the graph as a dictionary keyed by the node ids.