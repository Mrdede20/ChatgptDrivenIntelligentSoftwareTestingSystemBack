
def topological_ordering(nodes):
    ordered_nodes = []
    visited = set()
    def dfs(node):
        visited.add(node)
        for successor in node.outgoing_nodes:
            if successor not in visited:
                dfs(successor)
        ordered_nodes.append(node)
    for node in nodes:
        if node not in visited:
            dfs(node)
    ordered_nodes.reverse()
    return ordered_nodes
