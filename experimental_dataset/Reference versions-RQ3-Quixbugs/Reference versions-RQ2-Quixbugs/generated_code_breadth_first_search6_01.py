
from collections import deque

def bfs(startnode, goalnode):
    visited = set()
    queue = deque([startnode])
    while queue:
        node = queue.popleft()
        if node == goalnode:
            return True
        visited.add(node)
        for neighbor in node.successors:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
