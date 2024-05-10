
def topo_sort(nodes):
    ordered_nodes = []
    ready_nodes = []

    for node in nodes:
        if not node.incoming_nodes:
            ready_nodes.append(node)

    while ready_nodes:
        node = ready_nodes.pop(0)
        ordered_nodes.append(node)

        for successor in node.outgoing_nodes:
            successor.incoming_nodes.remove(node)

            if not successor.incoming_nodes:
                ready_nodes.append(successor)

    return ordered_nodes
