Here are two programs that achieve the same intention:

Program 1:

```python
import math
from FibonacciHeap import FibonacciHeap

class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def successor(self):
        return self.successor

    def successors(self):
        return self.successors

    def predecessors(self):
        return self.predecessors

def shortest_path_length(length_by_edge, startnode, goalnode):
    heap = FibonacciHeap()
    heap.insert(startnode, 0)
    visited = set()

    while heap:
        current_node, current_dist = heap.extract_min()
        if current_node == goalnode:
            return current_dist

        visited.add(current_node)

        for neighbor in current_node.successors:
            if neighbor in visited:
                continue

            edge = (current_node, neighbor)
            edge_length = length_by_edge[edge]
            neighbor_dist = current_dist + edge_length

            if neighbor in heap:
                heap.decrease_key(neighbor, min(neighbor_dist, heap.get_node_value(neighbor)))
            else:
                heap.insert(neighbor, neighbor_dist)

    return math.inf
```

Program 2:

```python
import math
from heapq import heappop, heappush

class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def successor(self):
        return self.successor

    def successors(self):
        return self.successors

    def predecessors(self):
        return self.predecessors

def shortest_path_length(length_by_edge, startnode, goalnode):
    heap = [(0, startnode)]
    visited = set()

    while heap:
        current_dist, current_node = heappop(heap)
        if current_node == goalnode:
            return current_dist

        visited.add(current_node)

        for neighbor in current_node.successors:
            if neighbor in visited:
                continue

            edge = (current_node, neighbor)
            edge_length = length_by_edge[edge]
            neighbor_dist = current_dist + edge_length

            if any(neighbor in node for _, node in heap):
                heap = [(d, n) if n != neighbor else (min(d, neighbor_dist), n) for d, n in heap]
                heapify(heap)
            else:
                heappush(heap, (neighbor_dist, neighbor))

    return math.inf
```