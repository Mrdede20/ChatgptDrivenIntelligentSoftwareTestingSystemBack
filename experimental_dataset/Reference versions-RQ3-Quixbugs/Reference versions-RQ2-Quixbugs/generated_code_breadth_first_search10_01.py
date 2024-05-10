
from collections import deque

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

def is_reachable_bfs(startnode, goalnode):
    visited = set()
    queue = deque([startnode])
    while queue:
        current_node = queue.popleft()
        if current_node == goalnode:
            return True
        visited.add(current_node)
        for successor in current_node.successors:
            if successor not in visited:
                queue.append(successor)
    return False
