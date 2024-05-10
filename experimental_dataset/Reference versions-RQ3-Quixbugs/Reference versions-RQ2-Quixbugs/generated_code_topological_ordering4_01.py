
def topo_sort(nodes):
    ordered_nodes = []
    ready_nodes = [node for node in nodes if not node.predecessors]

    while ready_nodes:
        node = ready_nodes.pop(0)
        ordered_nodes.append(node)

        for successor in node.successors:
            node.outgoing_nodes.remove(successor)
            successor.incoming_nodes.remove(node)

            if not successor.predecessors:
                ready_nodes.append(successor)

    return ordered_nodes
