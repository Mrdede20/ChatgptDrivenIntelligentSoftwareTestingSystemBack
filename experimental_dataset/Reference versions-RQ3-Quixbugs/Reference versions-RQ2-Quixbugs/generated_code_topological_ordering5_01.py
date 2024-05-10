
from collections import deque

def topological_sort(nodes):
    ordered_nodes = []
    no_incoming_nodes = deque([node for node in nodes if not node.incoming_nodes])
    
    while no_incoming_nodes:
        node = no_incoming_nodes.popleft()
        ordered_nodes.append(node)
        
        for outgoing_node in node.outgoing_nodes:
            outgoing_node.incoming_nodes.remove(node)
            if not outgoing_node.incoming_nodes:
                no_incoming_nodes.append(outgoing_node)
    
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Graph contains a cycle")
    
    return ordered_nodes
