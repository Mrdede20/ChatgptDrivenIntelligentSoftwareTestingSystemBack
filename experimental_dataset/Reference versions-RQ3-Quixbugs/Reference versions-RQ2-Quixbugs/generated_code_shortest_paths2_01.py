
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
