
from collections import deque

def bfs(startnode, goalnode):
    visited = set()
    queue = deque([startnode])
    while queue:
        node = queue.popleft()
        if node == goalnode:
            return True
        visited.add(node)
        for n in node.successors:
            if n not in visited:
                queue.append(n)
    return False
