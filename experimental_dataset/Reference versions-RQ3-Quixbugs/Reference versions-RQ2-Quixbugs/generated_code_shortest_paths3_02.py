
from collections import defaultdict


def bellman_ford_algorithm(graph, source):
    weight_by_node = defaultdict(lambda: float('inf'))
    weight_by_node[source] = 0
    
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if weight_by_node[node] + weight < weight_by_node[neighbor]:
                    weight_by_node[neighbor] = weight_by_node[node] + weight
    
    return weight_by_node
