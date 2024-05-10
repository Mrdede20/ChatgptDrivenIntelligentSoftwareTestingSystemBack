
def depth_first_search(start_node, goal_node, visited=set()):
    visited.add(start_node)
    if start_node == goal_node:
        return True
    for successor in start_node.successors:
        if successor not in visited:
            if depth_first_search(successor, goal_node, visited):
                return True
    return False
