
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
