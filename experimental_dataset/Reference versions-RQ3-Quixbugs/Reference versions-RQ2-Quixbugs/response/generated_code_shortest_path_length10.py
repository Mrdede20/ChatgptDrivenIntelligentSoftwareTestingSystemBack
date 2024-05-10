Sure, here are two implementations of the `shortest_path_length` function using the same method name and parameter types:

Implementation 1:

```
import math

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
    heap = FibHeap()
    visited = set()
    distance = {startnode: 0}

    heap.insert(startnode, 0)

    while heap:
        node, dist = heap.extract_min()

        if node == goalnode:
            return dist

        if node in visited:
            continue
        
        visited.add(node)

        for neighbor in node.successors:
            if neighbor in distance:
                if distance[neighbor] > dist + length_by_edge[(node, neighbor)]:
                    distance[neighbor] = dist + length_by_edge[(node, neighbor)]
                    heap.insert_or_update(neighbor, distance[neighbor])
            else:
                distance[neighbor] = dist + length_by_edge[(node, neighbor)]
                heap.insert(neighbor, distance[neighbor])

    return math.inf
```

Implementation 2:

```
import math

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
    heap = FibHeap()
    visited = set()
    distance = {startnode: 0}

    heap.insert(startnode, 0)

    while heap:
        node, dist = heap.extract_min()

        if node == goalnode:
            return dist

        if node in visited:
            continue
        
        visited.add(node)

        for neighbor in node.successors:
            if neighbor not in distance:
                distance[neighbor] = math.inf
            
            if distance[neighbor] > dist + length_by_edge[(node, neighbor)]:
                distance[neighbor] = dist + length_by_edge[(node, neighbor)]
                heap.insert_or_update(neighbor, distance[neighbor])

    return math.inf
```

Both implementations use the same `Node` class and the same `shortest_path_length` method signature to achieve the desired functionality. However, Implementation 2 uses a slightly different approach by initializing all nodes with a distance of infinity first and updating them as necessary, while Implementation 1 initializes the starting node with a distance of 0 and directly adds its neighbors to the heap.