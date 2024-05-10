Program 1:

```
from math import inf

def shortest_paths(source, weights):
    n = len(weights)
    distances = {node: inf for node in range(n)}
    distances[source] = 0

    for _ in range(n - 1):
        for u, v in weights:
            if distances[u] + weights[u, v] < distances[v]:
                distances[v] = distances[u] + weights[u, v]

    return distances
```

Program 2: 

```
from math import inf

def shortest_paths(source, weights):
    n = len(weights)
    distances = {node: None for node in range(n)}
    distances[source] = 0

    for _ in range(n - 1):
        for u, v in weights:
            if distances[u] is not None and (distances[v] is None or distances[u] + weights[u, v] < distances[v]):
                distances[v] = distances[u] + weights[u, v]

    for u, v in weights:
        if distances[u] is not None and distances[u] + weights[u, v] < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distances
```

Note: Program 1 assumes that there are no negative-weight cycles in the graph, while Program 2 checks for negative-weight cycles and raises an error if one is found. Program 2 is slower due to the extra cycle check, but is more robust in the presence of negative-weight cycles.