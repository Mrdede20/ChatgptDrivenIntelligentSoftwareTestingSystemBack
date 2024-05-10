
def bfs_search(start_node, goal_node):
    queue = [start_node]
    visited = set()

    while queue:
        node = queue.pop(0)
        if node == goal_node:
            return True
        visited.add(node)
        for successor in node.successors:
            if successor not in visited:
                queue.append(successor)
    
    return False
