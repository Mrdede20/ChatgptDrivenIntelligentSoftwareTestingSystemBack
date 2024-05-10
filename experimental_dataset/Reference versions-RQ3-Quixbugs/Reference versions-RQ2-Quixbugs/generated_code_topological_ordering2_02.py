
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

def topological_sort(nodes):
    ordered_nodes = []
    # Find all nodes that have no incoming edges
    nodes_with_no_predecessors = [node for node in nodes if not node.predecessors]
    # Iterate over all nodes with no incoming edges
    while nodes_with_no_predecessors:
        # Add each node to the ordered list
        node = nodes_with_no_predecessors.pop()
        ordered_nodes.append(node)
        # Check for all outgoing nodes of the current node
        for successor in node.successors:
            # Remove the current node from its predecessors
            successor.predecessors.remove(node)
            # If the current node was the last predecessor of the successor,
            # add the successor to the list of nodes with no incoming edges
            if not successor.predecessors:
                nodes_with_no_predecessors.append(successor)
    # Check if there are cycles in the graph
    for node in nodes:
        if node.predecessors:
            raise ValueError("Input graph is cyclic.")
    return ordered_nodes
