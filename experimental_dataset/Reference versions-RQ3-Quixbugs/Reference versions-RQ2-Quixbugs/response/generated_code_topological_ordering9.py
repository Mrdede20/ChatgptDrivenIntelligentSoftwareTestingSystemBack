Here are two implementations of a topological sort using the same method name and parameter type:

Implementation 1:

```
def topological_sort(nodes):
    ordered_nodes = []
    sources = [node for node in nodes if not node.incoming_nodes]
    
    while sources:
        current = sources.pop(0)
        ordered_nodes.append(current)
        
        for successor in current.outgoing_nodes:
            successor.incoming_nodes.remove(current)
            if not successor.incoming_nodes:
                sources.append(successor)
    
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Graph contains at least one cycle")
    
    return ordered_nodes
```

Implementation 2:

```
def topological_sort(nodes):
    in_degrees = {node: 0 for node in nodes}
    for node in nodes:
        for successor in node.outgoing_nodes:
            in_degrees[successor] += 1
    
    sources = [node for node, degree in in_degrees.items() if degree == 0]
    ordered_nodes = []
    
    while sources:
        current = sources.pop(0)
        ordered_nodes.append(current)
        
        for successor in current.outgoing_nodes:
            in_degrees[successor] -= 1
            if in_degrees[successor] == 0:
                sources.append(successor)
    
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Graph contains at least one cycle")
        
    return ordered_nodes
```

Both implementations take in a list of nodes and return the nodes in a topological order. The first implementation uses the idea of identifying sources and adding nodes that have no incoming edges to an ordered list. The second implementation uses a dictionary to keep track of the incoming degrees of each node and removes nodes with no incoming edges in each iteration. Both implementations raise a `ValueError` if the input graph contains a cycle.