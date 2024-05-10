
def shortest_paths(source, edges):
    dist = {node: float('inf') for node in edges}
    dist[source] = 0
    for _ in range(len(edges) - 1):
        for u, v in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + edges[u, v]:
                dist[v] = dist[u] + edges[u, v]
    return dist
