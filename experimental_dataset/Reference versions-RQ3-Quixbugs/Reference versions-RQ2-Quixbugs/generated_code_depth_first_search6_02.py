
def depth_first_search(start_node, goal_node, visited=set()):
    visited.add(start_node)
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node == goal_node:
            return True
        for successor in node.successors:
            if successor not in visited:
                visited.add(successor)
                stack.append(successor)
    return False
