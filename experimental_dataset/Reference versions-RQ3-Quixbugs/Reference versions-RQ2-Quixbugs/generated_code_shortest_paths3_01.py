
def bellman_ford_algorithm(graph, source):
    weight_by_node = {node: float('inf') for node in graph}
    weight_by_node[source] = 0
    
    for _ in range(len(weight_by_node) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if weight_by_node[node] + weight < weight_by_node[neighbor]:
                    weight_by_node[neighbor] = weight_by_node[node] + weight
                    
    return weight_by_node
