
def depth_first_search(start_node, goal_node):
    visited = set()
    def dfs(current_node):
        if current_node == goal_node:
            return True
        if current_node in visited:
            return False
        visited.add(current_node)
        for successor in current_node.successors:
            if dfs(successor):
                return True
        return False

    return dfs(start_node)
