Sure, here are two programs that achieve the intention:

Program 1:

```python
def shortest_paths(source, edges):
    INF = float('inf')
    dist = {}
    for vertex in edges:
        dist[vertex] = INF
    dist[source] = 0
    for _ in range(len(edges)-1):
        for u, v in edges:
            if dist[u] != INF and dist[u] + edges[u, v] < dist[v]:
                dist[v] = dist[u] + edges[u, v]
    return dist
```

Program 2:

```python
def shortest_paths(source, edges):
    dist = {node: float('inf') for node in edges}
    dist[source] = 0
    for _ in range(len(edges) - 1):
        for u, v in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + edges[u, v]:
                dist[v] = dist[u] + edges[u, v]
    return dist
```

Both programs achieve the same goal, which is to implement the Bellman-Ford algorithm. They take two parameters as input – the source node and a dictionary containing the edge weights keyed by an ordered pair of node IDs. The function then iterates through all the edges in the graph and repeatedly relaxes them until the shortest path is found. The output of the function is a dictionary that contains the minimum path weights from the source node to every other node in the graph.