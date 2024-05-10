
def depth_first_search(start_node, goal_node):
    visited_nodes = set()
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        if current_node == goal_node:
            return True
        visited_nodes.add(current_node)
        for successor in current_node.successors:
            if successor not in visited_nodes:
                stack.append(successor)
    return False
