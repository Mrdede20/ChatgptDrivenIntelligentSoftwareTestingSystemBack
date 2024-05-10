
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

def insert_or_update(queue, node, distance):
    for i, (n, d) in enumerate(queue):
        if n == node:
            queue[i] = (n, distance)
            heapq.heapify(queue)
            return
    heapq.heappush(queue, (node, distance))

def get(queue, node):
    for n, d in queue:
        if n == node:
            return d
    return None

def shortest_path_length(length_by_edge, startnode, goalnode):
    visited_nodes = set()
    unvisited_nodes = [(startnode, 0)]

    while(unvisited_nodes):
        current_node, current_distance = heapq.heappop(unvisited_nodes)

        if current_node == goalnode:
            return current_distance

        visited_nodes.add(current_node)

        for successor_node in current_node.successors:
            if successor_node not in visited_nodes:
                distance = current_distance + length_by_edge[(current_node, successor_node)]
                if get(unvisited_nodes, successor_node) is not None:
                    if distance < get(unvisited_nodes, successor_node):
                        insert_or_update(unvisited_nodes, successor_node, distance)
                else:
                    heapq.heappush(unvisited_nodes, (successor_node, distance))
            
    return None
