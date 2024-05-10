
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
    queue = deque([startnode])
    nodesseen = set([startnode])

    while queue:
        currentnode = queue.popleft()
        if currentnode == goalnode:
            return True
        for successor in currentnode.successors:
            if successor not in nodesseen:
                queue.append(successor)
                nodesseen.add(successor)
    return False
