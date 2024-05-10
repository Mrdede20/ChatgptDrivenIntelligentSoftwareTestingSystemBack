
def topological_ordering(nodes):
    ordered_nodes = []
    nodes_no_incoming_edges = [node for node in nodes if not node.incoming_nodes]
    while nodes_no_incoming_edges:
        node = nodes_no_incoming_edges.pop(0)
        ordered_nodes.append(node)
        for successor in node.outgoing_nodes:
            successor.incoming_nodes.remove(node)
            if not successor.incoming_nodes:
                nodes_no_incoming_edges.append(successor)
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Graph contains a cycle.")
    return ordered_nodes
