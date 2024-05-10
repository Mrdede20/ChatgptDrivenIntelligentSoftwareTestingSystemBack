
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
