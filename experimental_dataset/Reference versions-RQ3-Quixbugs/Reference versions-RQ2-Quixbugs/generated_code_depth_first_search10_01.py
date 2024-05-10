
def depth_first_search(start_node, goal_node, visited_nodes=set()):
    visited_nodes.add(start_node)
    if start_node == goal_node:
        return True
    for successor in start_node.successors:
        if successor not in visited_nodes:
            if depth_first_search(successor, goal_node, visited_nodes):
                return True
    return False
