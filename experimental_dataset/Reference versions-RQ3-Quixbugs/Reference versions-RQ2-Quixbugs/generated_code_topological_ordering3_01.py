
def topological_sort(nodes):
    # Dictionary to hold nodes and their visited status
    visited = {}
    # List to hold the sorted order
    order = []

    # Recursive helper function to perform depth-first search
    def dfs(node):
        # Mark the node as visited
        visited[node] = True
        # Visit each successor node that has not been visited
        for successor in node.successors:
            if successor not in visited:
                dfs(successor)
        # Add the node to the sorted order
        order.append(node)

    # Visit each unvisited node
    for node in nodes:
        if node not in visited:
            dfs(node)

    # Reverse the list to get the correct order
    order.reverse()
    return order
