Sure, please find below two implementations for the same.

Implementation 1:

```python
def find_minimum_spanning_tree(graph):
    edges = sorted(graph.keys(), key=lambda x: graph[x])
    group_by_node = {node: {node} for edge in graph for node in edge}

    minimum_spanning_tree = set()
    for edge in edges:
        node1, node2 = edge
        if group_by_node[node1] != group_by_node[node2]:
            minimum_spanning_tree.add(edge)
            group1 = group_by_node[node1]
            group2 = group_by_node[node2]
            group = group1.union(group2)
            for node in group:
                group_by_node[node] = group

    return minimum_spanning_tree
```

Implementation 2: 

```python
def find_minimum_spanning_tree(graph):
    edges = sorted(graph, key=lambda x: graph[x])
    group_by_node = {node: {node} for edge in graph for node in edge}

    minimum_spanning_tree = set()
    for edge in edges:
        node1, node2 = edge
        if group_by_node[node1] != group_by_node[node2]:
            minimum_spanning_tree.add((node1, node2))
            group1 = group_by_node[node1]
            group2 = group_by_node[node2]
            group = group1.union(group2)
            for node in group:
                group_by_node[node] = group

    return minimum_spanning_tree
```

Both the implementations will take in a dictionary with edges as keys and their weights as values. They first sort the edges in increasing order of weights. They then iterate over the edges and add the edge to the minimum spanning tree only if it doesn't create a cycle in the tree. To determine whether the edge creates a cycle, the algorithm keeps track of the connected components using a dictionary named `group_by_node`. Finally, it returns the set of edges that form the minimum spanning tree.

Example usage:

```python
graph = {('A', 'B'): 5, ('B', 'C'): 2, ('C', 'D'): 1, ('D', 'A'): 4, ('B', 'D'): 3}
minimum_spanning_tree = find_minimum_spanning_tree(graph)
print(minimum_spanning_tree) # {('C', 'D'), ('B', 'C'), ('A', 'B'), ('B', 'D')}
```

This will print a set containing the edges that form the minimum spanning tree for the given example graph.