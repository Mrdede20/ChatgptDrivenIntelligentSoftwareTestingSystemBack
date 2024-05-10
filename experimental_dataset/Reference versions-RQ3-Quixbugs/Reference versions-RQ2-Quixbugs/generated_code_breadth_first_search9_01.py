
from collections import deque

def bfs(start_node, goal_node):
    queue = deque()
    queue.append(start_node)
    visited = set()
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        if node == goal_node:
            return True
        for successor in node.successors:
            if successor not in visited:
                visited.add(successor)
                queue.append(successor)
    
    return False
