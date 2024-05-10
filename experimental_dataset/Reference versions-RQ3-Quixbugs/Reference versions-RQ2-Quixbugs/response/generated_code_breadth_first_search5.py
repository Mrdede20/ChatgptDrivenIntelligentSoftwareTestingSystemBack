Sure, here are two programs that implement the Breadth-First Search algorithm using the Node class:

Program 1:
```python
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
```

Program 2:
```python
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
```

Both programs start by creating a set to keep track of visited nodes and either a deque or a queue to store the nodes that still need to be visited. The while loop continues until the queue is empty, meaning that all nodes that can be reached from the startnode have been visited.

Within the loop, the next node is retrieved with either `popleft()` or `get()` depending on whether a deque or queue is used. If this node is the goalnode, the function returns True. Otherwise, it is added to the set of visited nodes and its successors are added to the queue (or deque) if they have not been visited before. Finally, if the loop completes without finding the goalnode, the function returns False.