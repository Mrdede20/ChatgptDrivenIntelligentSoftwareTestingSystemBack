
def dfs_search(start_node, goal_node):
    visited = set()
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node == goal_node:
            return True
        visited.add(node)
        for successor in node.successors:
            if successor not in visited:
                stack.append(successor)
                
    return False
