Program 1:

```
import heapq

class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes
        
def shortest_path_length(length_by_edge, startnode, goalnode):
    visited = set()
    heap = [(0, startnode)]
    while heap:
        (distance, node) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == goalnode:
            return distance
        for neighbor in node.successors:
            if neighbor not in visited:
                heapq.heappush(heap, (distance + length_by_edge[(node, neighbor)], neighbor))
    return None
```

Program 2:

```
import heapq

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
    visited = set()
    heap = [(0, startnode)]
    while heap:
        (distance, node) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == goalnode:
            return distance
        for neighbor in node.successors:
            if neighbor not in visited:
                heapq.heappush(heap, (distance + length_by_edge[(node, neighbor)], neighbor))
    return None
```

Both the programs implement the function `shortest_path_length` which uses Dijkstra's algorithm to find the shortest path between two nodes in a directed graph. The input arguments are `length_by_edge`, `startnode` and `goalnode`. The function uses `heapq` module to maintain a priority queue of unvisited nodes. At each iteration, it dequeues the node with the smallest accumulated distance from the start node and updates the distances of its neighbors. The function returns the distance of the shortest path between `startnode` and `goalnode`. The class `Node` is defined with some attributes and methods. Both programs use the same class and function name and have the same parameter type.