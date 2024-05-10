
def dfs(startnode, goalnode):
    visited = set()
    stack = [startnode]

    while stack:
        current = stack.pop()
        
        if current == goalnode:
            return True
        
        visited.add(current)

        for neighbor in current.successors:
            if neighbor not in visited:
                stack.append(neighbor)

    return False
