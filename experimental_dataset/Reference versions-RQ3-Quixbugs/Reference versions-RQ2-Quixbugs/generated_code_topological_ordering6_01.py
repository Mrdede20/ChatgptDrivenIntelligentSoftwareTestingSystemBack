
def topological_sort(nodes):
    # Initialize an empty list for the topologically sorted order
    order = []
    # Create a dictionary to keep track of each node's incoming edges
    incoming_edges = {node: 0 for node in nodes}
    # Create a dictionary to keep track of each node's outgoing edges
    outgoing_edges = {node: [] for node in nodes}
    # Populate the incoming and outgoing edge dictionaries
    for node in nodes:
        for successor in node.successors:
            incoming_edges[successor] += 1
            outgoing_edges[node].append(successor)
    # Create a queue of nodes with no incoming edges
    queue = [node for node in nodes if incoming_edges[node] == 0]
    # Begin the topological sort
    while queue:
        # Get the next node with no incoming edges
        node = queue.pop(0)
        # Add the node to the sorted order
        order.append(node)
        # Remove the node and its edges from the graph
        for successor in outgoing_edges[node]:
            incoming_edges[successor] -= 1
            if incoming_edges[successor] == 0:
                queue.append(successor)
    return order
