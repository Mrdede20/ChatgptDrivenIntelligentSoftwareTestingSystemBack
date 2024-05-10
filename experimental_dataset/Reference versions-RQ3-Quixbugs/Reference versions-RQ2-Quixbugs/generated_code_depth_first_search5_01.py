
def search_from(start_node, goal_node, visited_set=set()):
    visited_set.add(start_node)
    if start_node == goal_node:
        return True
    for successor in start_node.successors:
        if successor not in visited_set:
            if search_from(successor, goal_node, visited_set):
                return True
    return False
