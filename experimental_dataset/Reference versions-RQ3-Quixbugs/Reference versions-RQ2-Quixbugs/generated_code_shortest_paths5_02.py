
def shortest_paths(source, weight_by_edge):
    weight_by_node = {}
    for edge in weight_by_edge:
        weight_by_node[edge[0]] = float('inf')
        weight_by_node[edge[1]] = float('inf')
    weight_by_node[source] = 0
    for i in range(len(weight_by_node) - 1):
        changed = False
        for edge in weight_by_edge:
            if weight_by_node[edge[0]] + weight_by_edge[edge] < weight_by_node[edge[1]]:
                weight_by_node[edge[1]] = weight_by_node[edge[0]] + weight_by_edge[edge]
                changed = True
        if not changed:
            break
    return weight_by_node
