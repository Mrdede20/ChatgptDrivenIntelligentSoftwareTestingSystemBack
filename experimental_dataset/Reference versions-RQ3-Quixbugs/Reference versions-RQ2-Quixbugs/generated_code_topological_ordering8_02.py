
def topo_sort(nodes):
    # Create empty list to store the sorted nodes
    sorted_nodes = []
    
    # Create a set of nodes with no incoming edges
    root_nodes = set()
    for node in nodes:
        if not node.predecessors:
            root_nodes.add(node)
            
    # Traverse the graph
    while root_nodes:
        current_node = root_nodes.pop()
        sorted_nodes.append(current_node)

        for successor in current_node.successors:
            # Remove current_node from its successor's predecessors
            successor.predecessors.remove(current_node)

            # Add successor to the set of root nodes if it has no more predecessors
            if not successor.predecessors:
                root_nodes.add(successor)

    # Check for cycles
    if len(sorted_nodes) != len(nodes):
        raise ValueError("Graph contains cycles")

    return sorted_nodes
