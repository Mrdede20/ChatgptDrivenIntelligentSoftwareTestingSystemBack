
def topological_sort(nodes):
    in_degrees = {node: 0 for node in nodes}
    for node in nodes:
        for successor in node.outgoing_nodes:
            in_degrees[successor] += 1
    
    sources = [node for node, degree in in_degrees.items() if degree == 0]
    ordered_nodes = []
    
    while sources:
        current = sources.pop(0)
        ordered_nodes.append(current)
        
        for successor in current.outgoing_nodes:
            in_degrees[successor] -= 1
            if in_degrees[successor] == 0:
                sources.append(successor)
    
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Graph contains at least one cycle")
        
    return ordered_nodes
