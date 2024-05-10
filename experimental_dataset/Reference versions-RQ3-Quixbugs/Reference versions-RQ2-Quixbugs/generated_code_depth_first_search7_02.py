
def dfs_search(start_node, goal_node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start_node)
    
    if start_node == goal_node:
        return True
    
    for successor in start_node.successors:
        if successor not in visited:
            found = dfs_search(successor, goal_node, visited)
            if found:
                return True
    
    return False
