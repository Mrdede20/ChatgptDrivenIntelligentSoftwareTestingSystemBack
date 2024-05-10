
def topological_sort(nodes):
    # Dictionary to hold nodes and their visited status
    visited = {}
    # List to hold the sorted order
    order = []
    # Stack to hold nodes that have not been fully processed
    stack = []

    # Add each node to the stack
    for node in nodes:
        stack.append(node)

    # Loop until the stack is empty
    while stack:
        # Get the next node from the stack
        node = stack.pop()
        # Check if the node has already been visited
        if node in visited:
            continue
        # Mark the node as visited
        visited[node] = True
        # Add each unvisited successor to the stack
        for successor in node.successors:
            if successor not in visited:
                stack.append(successor)
        # Add the node to the sorted order
        order.append(node)

    # Reverse the list to get the correct order
    order.reverse()
    return order
