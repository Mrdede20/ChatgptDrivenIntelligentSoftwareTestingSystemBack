Sure, here are two implementations of the Floyd-Warshall algorithm in Python:

First Implementation:

```python
from collections import defaultdict


def floyd_warshall(n, length_by_edge):
    # Create a defaultdict object to hold the shortest path lengths
    shortest_paths = defaultdict(lambda: defaultdict(lambda: float('inf')))
    
    # Set the initial distances between nodes
    for node, edges in length_by_edge.items():
        for neighbor, distance in edges.items():
            shortest_paths[node][neighbor] = distance
            
    # Iterate through every node and update shortest path lengths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                shortest_paths[i][j] = min(shortest_paths[i][j], 
                                           shortest_paths[i][k] + shortest_paths[k][j])
    
    # Return the dictionary of shortest path lengths
    return shortest_paths
```

Second Implementation:

```python
from collections import defaultdict


def floyd_warshall(n, length_by_edge):
    # Create a defaultdict object to hold the shortest path lengths
    shortest_paths = defaultdict(lambda: defaultdict(lambda: float('inf')))
    
    # Set the initial distances between nodes
    for node, edges in length_by_edge.items():
        for neighbor, distance in edges.items():
            shortest_paths[node][neighbor] = distance
            
    # Iterate through every node and update shortest path lengths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if shortest_paths[i][j] > shortest_paths[i][k] + shortest_paths[k][j]:
                    shortest_paths[i][j] = shortest_paths[i][k] + shortest_paths[k][j]
    
    # Return the dictionary of shortest path lengths
    return shortest_paths
```

Both implementations accomplish the same thing - they take in the number of nodes `n` and the dictionary `length_by_edge` which describes the length of edges between nodes, and they return a dictionary of the shortest path lengths between all pairs of nodes. 

The first implementation updates the shortest path lengths for every pair of nodes, regardless of whether a shorter path has been found. The second implementation only updates the shortest path if a shorter path has been found. The second implementation may be slightly more efficient, since it avoids unnecessary updates.