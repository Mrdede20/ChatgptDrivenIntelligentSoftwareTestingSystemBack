Program 1:

```
def bellman_ford(source, edges):
    distance = {node: float('inf') for node in edges}
    distance[source] = 0
    
    for _ in range(len(edges)-1):
        for u, neighbors in edges.items():
            for v, weight in neighbors.items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    
    for u, neighbors in edges.items():
        for v, weight in neighbors.items():
            if distance[u] + weight < distance[v]:
                raise ValueError('Negative weight cycle detected')
    
    return distance
```

Program 2:

```
def bellman_ford(source, edges):
    distance = {node: float('inf') for node in edges}
    distance[source] = 0
    
    for i in range(len(edges)-1):
        for u in edges:
            for v in edges[u]:
                if distance[v] > distance[u] + edges[u][v]:
                    distance[v] = distance[u] + edges[u][v]
    
    for u in edges:
        for v in edges[u]:
            if distance[v] > distance[u] + edges[u][v]:
                raise ValueError('Negative weight cycle detected')
    
    return distance
```

Both of these programs take a source node and a dictionary of edges weights as input and implement the Bellman-Ford algorithm to compute the minimum weight of a path from the source node to every other node in the graph. The algorithm stops either when it has reached the minimum distance to each node or detects a negative-weight cycle.

Program 1 uses nested for loops to iterate through each edge in the graph and updates the distance to each node. It then checks for negative-weight cycle.

Program 2 is a bit more compact and easier to read. It also uses nested for loops to iterate through each edge in the graph, but it updates the distance to each node in a slightly different way, and also checks for negative-weight cycle in a slightly different way.

Both programs should produce the same result for the same input data, but one of them may be faster or more efficient than the other depending on the size and complexity of the graph being used.