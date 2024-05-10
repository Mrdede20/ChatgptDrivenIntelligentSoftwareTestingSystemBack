Here's the first program to implement the Bellman-Ford algorithm:

```
def shortest_paths(source, weight_by_edge):
    weight_by_node = {}
    for edge in weight_by_edge:
        weight_by_node[edge[0]] = float('inf')
        weight_by_node[edge[1]] = float('inf')
    weight_by_node[source] = 0
    for i in range(len(weight_by_node) - 1):
        for edge in weight_by_edge:
            if weight_by_node[edge[0]] + weight_by_edge[edge] < weight_by_node[edge[1]]:
                weight_by_node[edge[1]] = weight_by_node[edge[0]] + weight_by_edge[edge]
    return weight_by_node
```

Here's the second program to implement the Bellman-Ford algorithm with an optimization:

```
def shortest_paths(source, weight_by_edge):
    weight_by_node = {}
    for edge in weight_by_edge:
        weight_by_node[edge[0]] = float('inf')
        weight_by_node[edge[1]] = float('inf')
    weight_by_node[source] = 0
    for i in range(len(weight_by_node) - 1):
        changed = False
        for edge in weight_by_edge:
            if weight_by_node[edge[0]] + weight_by_edge[edge] < weight_by_node[edge[1]]:
                weight_by_node[edge[1]] = weight_by_node[edge[0]] + weight_by_edge[edge]
                changed = True
        if not changed:
            break
    return weight_by_node
```

The second program has an optimization where it only iterates `len(weight_by_node) - 1` times if there are no changes to the weights of the nodes in the previous iteration. This is because if there are no changes, then the algorithm has already converged and there is no need to continue iterating.