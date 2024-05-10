
def topo_sort(nodes):
    incoming_nodes = {}
    outgoing_nodes = {}

    for node in nodes:
        incoming_nodes[node] = set()
        outgoing_nodes[node] = set()

    for node in nodes:
        for successor in node.successors:
            incoming_nodes[successor].add(node)
            outgoing_nodes[node].add(successor)

    ordered_nodes = []

    while incoming_nodes:
        node_with_no_incoming_edges = None
        for node in incoming_nodes:
            if not incoming_nodes[node]:
                node_with_no_incoming_edges = node
                break

        if node_with_no_incoming_edges is None:
            raise ValueError("Input graph is not acyclic")

        ordered_nodes.append(node_with_no_incoming_edges)
        del incoming_nodes[node_with_no_incoming_edges]
        for successor in outgoing_nodes[node_with_no_incoming_edges]:
            incoming_nodes[successor].remove(node_with_no_incoming_edges)

    return ordered_nodes
