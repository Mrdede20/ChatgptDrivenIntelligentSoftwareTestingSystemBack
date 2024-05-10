
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
