
def topological_sort(nodes):
    ordered_nodes = []
    sources = [node for node in nodes if not node.incoming_nodes]
    
    while sources:
        current = sources.pop(0)
        ordered_nodes.append(current)
        
        for successor in current.outgoing_nodes:
            successor.incoming_nodes.remove(current)
            if not successor.incoming_nodes:
                sources.append(successor)
    
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Graph contains at least one cycle")
    
    return ordered_nodes
