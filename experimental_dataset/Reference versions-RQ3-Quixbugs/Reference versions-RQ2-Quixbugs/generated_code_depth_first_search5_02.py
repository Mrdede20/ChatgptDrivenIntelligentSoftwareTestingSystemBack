
def search_from(start_node, goal_node, visited_set=set()):
    visited_set.add(start_node)
    for successor in start_node.successors:
        if successor not in visited_set:
            if successor == goal_node or search_from(successor, goal_node, visited_set):
                return True
    return False
