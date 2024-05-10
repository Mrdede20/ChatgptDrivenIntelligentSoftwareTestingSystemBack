
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

def breadth_first_search(startnode, goalnode):
    queue = deque()
    queue.append(startnode)
    nodesseen = set()
    nodesseen.add(startnode)

    while queue:
        current = queue.popleft()
        if current == goalnode:
            return True
        for successor in current.successors:
            if successor not in nodesseen:
                nodesseen.add(successor)
                queue.append(successor)
    return False
