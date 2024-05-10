
from queue import Queue

def bfs(start_node, goal_node):
    queue = Queue()
    queue.put(start_node)
    visited = set()
    visited.add(start_node)

    while not queue.empty():
        node = queue.get()
        if node == goal_node:
            return True
        for successor in node.successors:
            if successor not in visited:
                visited.add(successor)
                queue.put(successor)
    
    return False
