
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
    # Create a stack to store nodes with no outgoing edges
    stack = [node for node in nodes if not outgoing_edges[node]]
    # Begin the topological sort
    while stack:
        # Get the next node with no outgoing edges
        node = stack.pop()
        # Add the node to the sorted order
        order.append(node)
        # Remove the node and its edges from the graph
        for predecessor in node.predecessors:
            outgoing_edges[predecessor].remove(node)
            if not outgoing_edges[predecessor]:
                stack.append(predecessor)
    return order[::-1]
