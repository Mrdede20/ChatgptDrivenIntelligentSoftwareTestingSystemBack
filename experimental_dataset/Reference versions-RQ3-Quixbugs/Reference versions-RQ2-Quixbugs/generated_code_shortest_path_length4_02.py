
import queue

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
    distances = {startnode: 0}
    q = queue.PriorityQueue()
    q.put((0, startnode))
    while not q.empty():
        (dist, current_node) = q.get()
        if current_node == goalnode:
            return dist
        for successor, successor_dist in length_by_edge[current_node].items():
            new_dist = dist + successor_dist
            if successor not in distances or new_dist < distances[successor]:
                distances[successor] = new_dist
                q.put((new_dist, successor))
    return float('inf')
