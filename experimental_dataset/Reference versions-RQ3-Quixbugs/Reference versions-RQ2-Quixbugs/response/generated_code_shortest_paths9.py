Sure, here are two programs using the Bellman-Ford algorithm to find the minimum weight path from the source node to every other node in a directed graph:

Program 1:

```python
def bellman_ford(source, edges_weights):
    # Initialize the minimum distances from source to all nodes as infinity
    distances = {node: float('inf') for node in edges_weights.keys()}
    distances[source] = 0
    
    # Iterate through all edges and update the distances if a shorter path is found
    for _ in range(len(edges_weights)):
        for (u, v), weight in edges_weights.items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative-weight cycles
    for (u, v), weight in edges_weights.items():
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    
    return distances
```

Program 2:

```python
def bellman_ford(source, edges_weights):
    # Initialize the minimum distances from source to all nodes as infinity
    distances = {node: float('inf') for node in edges_weights.keys()}
    distances[source] = 0
    
    # Iterate through all edges (V-1) times and update the distances if a shorter path is found
    for i in range(len(edges_weights)-1):
        for (u, v), weight in edges_weights.items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative-weight cycles
    for (u, v), weight in edges_weights.items():
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    
    return distances
```

Both programs have the same function name and parameter types, and they use the same algorithm to calculate the minimum weight path from a source node to every other node in a directed graph. The difference lies in the number of iterations: program 1 iterates through all edges V times, while program 2 iterates through all edges V-1 times. Program 2 is more efficient but assumes no negative-weight cycles.