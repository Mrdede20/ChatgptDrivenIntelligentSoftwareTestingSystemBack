Program 1:

```
import math

def bellman_ford(source, edges):
    distance = dict()
    for node in edges:
        distance[node] = math.inf
    distance[source] = 0

    for i in range(len(edges)-1):
        for edge in edges:
            u, v = edge
            if distance[u] != math.inf and distance[u] + edges[edge] < distance[v]:
                distance[v] = distance[u] + edges[edge]

    return distance
```

Program 2:

```
import sys

def bellman_ford(source, edges):
    distance = dict()
    for node in edges:
        distance[node] = sys.maxsize
    distance[source] = 0

    for _ in range(len(edges) - 1):
        for u, v in edges:
            if distance[u] != sys.maxsize and distance[u] + edges[(u, v)] < distance[v]:
                distance[v] = distance[u] + edges[(u, v)]

    return distance
```

Both programs use the same method name `bellman_ford` and the same input parameters: the source node id and a dictionary containing edge weights keyed by an ordered pair of node ids. The output is a dictionary mapping each node id to the minimum weight of a path from the source node to that node.

The first program uses the `math.inf` constant to initialize the node weights to infinity, while the second program uses `sys.maxsize`. Both programs iterate through the edge dictionary until there is no further improvement.