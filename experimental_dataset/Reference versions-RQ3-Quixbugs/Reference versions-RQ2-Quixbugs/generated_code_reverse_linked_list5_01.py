
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


def reverse_linked_list(head):
    current_node = head
    previous_node = None
    next_node = None

    while current_node:
        next_node = current_node.successor
        current_node.successor = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node
