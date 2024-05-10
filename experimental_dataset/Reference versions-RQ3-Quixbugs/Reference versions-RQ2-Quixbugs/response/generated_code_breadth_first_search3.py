Here are the two programs that implement the Breadth-First Search algorithm to find whether the goal node is reachable from the start node in a directed graph. Both programs use the same method name and the same parameter type as specified in the problem statement.

Program 1:

```python
from collections import deque

class Node:
    def __init__(self, value=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def is_reachable(self, start_node, goal_node):
        queue = deque([start_node])
        seen = set([start_node])

        while queue:
            current_node = queue.popleft()
            if current_node == goal_node:
                return True
            for successor in current_node.successors:
                if successor not in seen:
                    seen.add(successor)
                    queue.append(successor)
        return False
```

Program 2:

```python
from queue import Queue

class Node:
    def __init__(self, value=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def is_reachable(self, start_node, goal_node):
        queue = Queue()
        queue.put(start_node)
        seen = set([start_node])

        while not queue.empty():
            current_node = queue.get()
            if current_node == goal_node:
                return True
            for successor in current_node.successors:
                if successor not in seen:
                    seen.add(successor)
                    queue.put(successor)
        return False
```

Both programs use the Breadth-First Search algorithm to find the goal node in a directed graph. They use a queue to explore the graph and a set of seen nodes to keep track of the nodes that have already been explored. The difference between the two programs is the choice of the queue data structure used. Program 1 uses deque from the collections module, while Program 2 uses Queue from the queue module.