
from collections import defaultdict

def shortest_paths(source, weight_by_edge):

    # Initialize weight_by_node dictionary
    weight_by_node = defaultdict(lambda: float('inf'))
    weight_by_node[source] = 0

    # Apply Bellman-Ford algorithm
    for i in range(len(weight_by_node)-1):
        for edge, weight in weight_by_edge.items():
            u, v = edge[0], edge[1]
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    # Return weight_by_node dictionary
    return weight_by_node
