Here are two programs that implement the Bellman-Ford algorithm to find the shortest path from a source node to every other node in a weighted graph that may contain negative edges (as long as there are no negative-weight cycles):

Program 1:

```python
from collections import defaultdict

def shortest_paths(source, weight_by_edge):

    # Initialize weight_by_node dictionary
    weight_by_node = defaultdict(lambda: float('inf'))
    weight_by_node[source] = 0

    # Apply Bellman-Ford algorithm
    for i in range(len(weight_by_node)-1):
        for edge, weight in weight_by_edge.items():
            u, v = edge[0], edge[1]
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    # Return weight_by_node dictionary
    return weight_by_node
```

Program 2:

```python
from collections import defaultdict

def shortest_paths(source, weight_by_edge):

    # Initialize weight_by_node dictionary
    weight_by_node = defaultdict(lambda: float('inf'))
    weight_by_node[source] = 0

    # Apply Bellman-Ford algorithm
    for i in range(len(weight_by_edge)-1):
        for edge in weight_by_edge:
            u, v = edge[0], edge[1]
            if weight_by_node[u] + weight_by_edge[edge] < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight_by_edge[edge]

    # Return weight_by_node dictionary
    return weight_by_node
```

Both programs take the same inputs and return the same output as described in the problem statement. However, Program 1 loops over the range of the length of `weight_by_node`, while Program 2 loops over the keys in the `weight_by_edge` dictionary directly.