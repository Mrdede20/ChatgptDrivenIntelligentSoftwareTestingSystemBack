Here are two programs that implement the Bellman-Ford algorithm:

Program 1:

```
def bellman_ford(source, edges):
    # Initialize node weights with infinity for all nodes except source
    weights = {node: float('inf') for node in edges.keys()}
    weights[source] = 0
    
    # Perform V-1 iterations where V is the number of nodes
    for _ in range(len(edges)-1):
        # Iterate over all edges and update weights
        for (u, v), weight in edges.items():
            if weights[u] + weight < weights[v]:
                weights[v] = weights[u] + weight
    
    return weights
```

Program 2:

```
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
```

Both programs implement the Bellman-Ford algorithm and take a source node and a dictionary of edge weights as input, and return a dictionary mapping each node id to the minimum weight of a path from the source node to that node. The second program includes an optimization that terminates early if no weights were updated in an iteration, which can improve performance in some cases.