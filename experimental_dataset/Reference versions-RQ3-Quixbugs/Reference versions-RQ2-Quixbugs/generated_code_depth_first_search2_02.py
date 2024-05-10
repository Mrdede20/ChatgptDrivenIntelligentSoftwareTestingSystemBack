
def depth_first_search(start_node, goal_node, visited=set()):
    visited.add(start_node)
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        if current_node == goal_node:
            return True
        for node in current_node.successors:
            if node not in visited:
                visited.add(node)
                stack.append(node)
    return False
