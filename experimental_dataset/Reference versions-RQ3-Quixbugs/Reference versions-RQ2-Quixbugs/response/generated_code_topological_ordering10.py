Here are two programs that implement the topological sort algorithm using the given `Node` class:

Program 1:

```python
def topological_sort(nodes):
    ordered_nodes = []
    no_incoming_edges = [node for node in nodes if not node.incoming_nodes]
    while no_incoming_edges:
        node = no_incoming_edges.pop()
        ordered_nodes.append(node)
        for succ in node.successors:
            succ.incoming_nodes.remove(node)
            if not succ.incoming_nodes:
                no_incoming_edges.append(succ)
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Input graph is not acyclic!")
    return ordered_nodes
```

Program 2:

```python
def topological_sort(nodes):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for succ in node.successors:
            if succ not in visited:
                dfs(succ)
        stack.append(node)

    for node in nodes:
        if node not in visited:
            dfs(node)

    return list(reversed(stack))
```

Both programs take a list of `Node` objects as input and return a list of nodes in topological order. The first program uses a variation of the Kahn's algorithm, while the second program uses a depth-first search approach.