
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
