Program 1:

```python
def topological_ordering(nodes):
    ordered_nodes = []
    nodes_no_incoming_edges = [node for node in nodes if not node.incoming_nodes]
    while nodes_no_incoming_edges:
        node = nodes_no_incoming_edges.pop(0)
        ordered_nodes.append(node)
        for successor in node.outgoing_nodes:
            successor.incoming_nodes.remove(node)
            if not successor.incoming_nodes:
                nodes_no_incoming_edges.append(successor)
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Graph contains a cycle.")
    return ordered_nodes
```

Program 2:

```python
def topological_ordering(nodes):
    ordered_nodes = []
    visited = set()
    def dfs(node):
        visited.add(node)
        for successor in node.outgoing_nodes:
            if successor not in visited:
                dfs(successor)
        ordered_nodes.append(node)
    for node in nodes:
        if node not in visited:
            dfs(node)
    ordered_nodes.reverse()
    return ordered_nodes
```

Both programs implement the same topological ordering algorithm, but they achieve it in slightly different ways. The first program uses a queue to keep track of nodes that have no incoming edges and iteratively adds those nodes to the ordered list while updating the incoming edges of their successors. The second program uses a depth-first search to visit all of the nodes and adds them to the ordered list in reverse order. The second program also raises an error if the graph contains a cycle.