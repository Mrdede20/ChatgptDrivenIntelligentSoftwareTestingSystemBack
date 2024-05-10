
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
