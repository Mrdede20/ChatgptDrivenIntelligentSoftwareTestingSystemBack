
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
