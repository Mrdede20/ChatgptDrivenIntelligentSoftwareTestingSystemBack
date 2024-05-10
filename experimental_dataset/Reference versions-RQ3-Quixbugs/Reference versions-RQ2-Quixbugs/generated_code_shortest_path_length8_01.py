
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
