
def topo_sort(nodes):
    incoming_nodes = {node: set() for node in nodes}
    outgoing_nodes = {node: set() for node in nodes}

    for node in nodes:
        for successor in node.successors:
            incoming_nodes[successor].add(node)
            outgoing_nodes[node].add(successor)

    ordered_nodes = [node for node in nodes if not incoming_nodes[node]]

    for node in ordered_nodes:
        for successor in node.successors:
            incoming_nodes[successor].remove(node)
            if not incoming_nodes[successor]:
                ordered_nodes.append(successor)

    return ordered_nodes
