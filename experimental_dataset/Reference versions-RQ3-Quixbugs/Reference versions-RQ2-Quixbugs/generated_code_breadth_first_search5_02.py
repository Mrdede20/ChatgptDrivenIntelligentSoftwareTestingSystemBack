
from queue import Queue

def bfs(startnode, goalnode):
    visited = set()
    queue = Queue()
    queue.put(startnode)
    while not queue.empty():
        node = queue.get()
        if node == goalnode:
            return True
        visited.add(node)
        for n in node.successors:
            if n not in visited:
                queue.put(n)
    return False
