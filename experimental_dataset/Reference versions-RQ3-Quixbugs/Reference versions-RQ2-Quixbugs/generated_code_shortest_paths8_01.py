
def bellman_ford(source, edges):
    distance = {node: float('inf') for node in edges}
    distance[source] = 0
    
    for _ in range(len(edges)-1):
        for u, neighbors in edges.items():
            for v, weight in neighbors.items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    
    for u, neighbors in edges.items():
        for v, weight in neighbors.items():
            if distance[u] + weight < distance[v]:
                raise ValueError('Negative weight cycle detected')
    
    return distance
