
def topological_sort(nodes):
    ordered_nodes = []
    no_incoming_edges = [node for node in nodes if not node.incoming_nodes]
    while no_incoming_edges:
        node = no_incoming_edges.pop()
        ordered_nodes.append(node)
        for succ in node.successors:
            succ.incoming_nodes.remove(node)
            if not succ.incoming_nodes:
                no_incoming_edges.append(succ)
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Input graph is not acyclic!")
    return ordered_nodes
