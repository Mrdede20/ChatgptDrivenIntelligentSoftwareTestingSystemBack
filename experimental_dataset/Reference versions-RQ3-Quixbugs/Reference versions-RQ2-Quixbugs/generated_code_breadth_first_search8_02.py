
from collections import deque

class Node:
    def __init__(self, value=None, successor=None, successors=set(), predecessors=set(), incoming_nodes=set(), outgoing_nodes=set()):
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

def is_reachable(startnode: Node, goalnode: Node) -> bool:
    queue = deque([startnode])
    nodesseen = set()

    while queue:
        node = queue.popleft()
        if node == goalnode:
            return True
        nodesseen.add(node)
        for succ in node.successors:
            if succ not in nodesseen:
                queue.append(succ)

    return False
