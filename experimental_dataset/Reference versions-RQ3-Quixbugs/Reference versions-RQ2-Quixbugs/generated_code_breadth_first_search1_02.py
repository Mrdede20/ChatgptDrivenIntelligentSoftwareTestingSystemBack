
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


def bfs(startnode, goalnode):
    visited = set()
    queue = deque()
    queue.append(startnode)

    while queue:
        node = queue.popleft()
        if node == goalnode:
            return True
        visited.add(node)
        for neighbor in node.successors:
            if neighbor not in visited:
                queue.append(neighbor)

    return False
