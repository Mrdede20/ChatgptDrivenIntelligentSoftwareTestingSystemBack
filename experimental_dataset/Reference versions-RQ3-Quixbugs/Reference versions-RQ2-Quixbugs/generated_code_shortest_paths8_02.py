
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
