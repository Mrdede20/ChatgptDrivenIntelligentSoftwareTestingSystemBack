Sure, here are two implementations of Breadth-First-Search algorithm in Python using the provided `Node` class:

**Implementation 1:**

```
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
```

**Implementation 2:**

```
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
```

Both implementations use a queue to keep track of the nodes to visit next, and they mark the visited nodes using a set. The first implementation uses `deque` from `collections` module to create a double-ended queue, while the second implementation uses `Queue` from `queue` module. They both take the start and goal nodes as input and return True if the goal node is found, False otherwise.