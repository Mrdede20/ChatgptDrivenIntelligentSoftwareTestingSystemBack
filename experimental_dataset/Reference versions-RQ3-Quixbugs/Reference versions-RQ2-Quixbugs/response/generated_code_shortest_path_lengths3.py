Program 1:

```python
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
```

Program 2:

```python
from collections import defaultdict

def floyd_warshall(num_nodes, edges):
    # Initialize distance dictionary
    dist = defaultdict(lambda: float('inf'))
    for i in range(num_nodes):
        dist[(i, i)] = 0
    
    # Update distance dictionary
    for edge in edges:
        u, v = edge
        dist[(u, v)] = edges[edge]
    
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[(i, j)] = min(dist[(i, j)], dist[(i, k)] + dist[(k, j)])
    
    return dict(dist)
```

Both programs have the same method name and parameter types. They use the defaultdict object to handle the case when the distance between two nodes is not known. They initialize the distance between a node and itself to 0 and all other distances to infinity. They update these distances based on the length of the shortest path that goes through an intermediate node k using a nested loop that considers all possible intermediate nodes. Finally, they return a dictionary containing the shortest path length keyed by an ordered pair of node ids.