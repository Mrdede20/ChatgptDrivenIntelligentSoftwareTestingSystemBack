
def topological_sort(nodes):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for succ in node.successors:
            if succ not in visited:
                dfs(succ)
        stack.append(node)

    for node in nodes:
        if node not in visited:
            dfs(node)

    return list(reversed(stack))
