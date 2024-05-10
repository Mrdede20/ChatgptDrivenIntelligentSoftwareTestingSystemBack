Program 1:

```
def topo_sort(nodes):
    ordered_nodes = []
    ready_nodes = [node for node in nodes if not node.predecessors]

    while ready_nodes:
        node = ready_nodes.pop(0)
        ordered_nodes.append(node)

        for successor in node.successors:
            node.outgoing_nodes.remove(successor)
            successor.incoming_nodes.remove(node)

            if not successor.predecessors:
                ready_nodes.append(successor)

    return ordered_nodes
```

Program 2:

```
def topo_sort(nodes):
    ordered_nodes = []
    ready_nodes = []

    for node in nodes:
        if not node.incoming_nodes:
            ready_nodes.append(node)

    while ready_nodes:
        node = ready_nodes.pop(0)
        ordered_nodes.append(node)

        for successor in node.outgoing_nodes:
            successor.incoming_nodes.remove(node)

            if not successor.incoming_nodes:
                ready_nodes.append(successor)

    return ordered_nodes
```

Both programs achieve the same goal by performing a topological sort on a directed acyclic graph. They take in a list of `Node` objects and return a list of those nodes in an order such that every node appears before all the nodes it has edges to. The first program uses the `predecessors` and `successors` attributes of each `Node` object to keep track of incoming and outgoing edges. The second program uses the `incoming_nodes` and `outgoing_nodes` attributes instead.