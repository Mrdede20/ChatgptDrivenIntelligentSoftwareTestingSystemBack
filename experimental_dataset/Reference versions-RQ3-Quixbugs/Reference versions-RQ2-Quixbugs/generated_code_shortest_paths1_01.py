
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
