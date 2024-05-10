
def bellman_ford(source, edges):
    # Initialize node weights with infinity for all nodes except source
    weights = {node: float('inf') for node in edges.keys()}
    weights[source] = 0
    
    # Perform V-1 iterations where V is the number of nodes
    for _ in range(len(edges)-1):
        # Keep track of whether any weights were updated
        updated = False
        
        # Iterate over all edges and update weights
        for (u, v), weight in edges.items():
            if weights[u] + weight < weights[v]:
                weights[v] = weights[u] + weight
                updated = True
        
        # Terminate early if no weights were updated in this iteration
        if not updated:
            break
    
    return weights
