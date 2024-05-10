Program 1:

```python
from collections import deque

class Node:
    def __init__(self, value=None, successors=[]):
        self.value = value
        self.successors = successors

def bfs(start_node, goal_node):
    queue = deque([start_node])
    visited = set()
    
    while queue:
        current_node = queue.popleft()
        if current_node == goal_node:
            return True
        
        visited.add(current_node)
        
        for neighbor_node in current_node.successors:
            if neighbor_node not in visited:
                queue.append(neighbor_node)
    return False
```

Program 2:

```python
from queue import Queue

class Node:
    def __init__(self, value=None, successors=[]):
        self.value = value
        self.successors = successors

def bfs(start_node, goal_node):
    queue = Queue(maxsize=0)
    queue.put(start_node)
    visited = set()
    
    while not queue.empty():
        current_node = queue.get()
        if current_node == goal_node:
            return True
        
        visited.add(current_node)
        
        for neighbor_node in current_node.successors:
            if neighbor_node not in visited:
                queue.put(neighbor_node)
    return False
```
Both of these programs implement the Breadth-first search (BFS) algorithm to determine whether a goal node is reachable from a starting node in a directed graph. They use a queue data structure to keep track of the nodes to be visited next and a set data structure to keep track of nodes that have already been explored. The input to the function is a digraph represented by its nodes, along with the starting node and the goal node. The output is True if the goal node is reachable from the starting node and False otherwise.