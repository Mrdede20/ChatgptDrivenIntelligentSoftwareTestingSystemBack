
def dfs(startnode, goalnode):
    visited = set()

    def dfs_helper(current):
        visited.add(current)
        if current == goalnode:
            return True
        for neighbor in current.successors:
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    return True
        return False

    return dfs_helper(startnode)
