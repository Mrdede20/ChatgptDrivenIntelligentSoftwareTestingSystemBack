Here are 2 programs that achieve the same task using Kruskal's algorithm:

Program 1:

```
def minimum_spanning_tree(weight_by_edge):
    # Sort edges by weight
    edges = []
    for edge, weight in weight_by_edge.items():
        edges.append((weight, edge))
    edges.sort()

    # Create disjoint-set data structure
    group_by_node = {}
    for node in weight_by_edge.keys():
        group_by_node[node] = {node}

    # Loop through edges and add to minimum spanning tree if it doesn't create a cycle
    mst_edges = set()
    for weight, (node1, node2) in edges:
        if group_by_node[node1] != group_by_node[node2]:
            mst_edges.add((node1, node2))
            group_by_node[node1] |= group_by_node[node2]
            group_by_node[node2] = group_by_node[node1]

    # Return set of edges in minimum spanning tree
    return mst_edges
```

Program 2:

```
def minimum_spanning_tree(weight_by_edge):
    # Sort edges by weight
    edges = sorted(weight_by_edge.items(), key=lambda x: x[1])

    # Create disjoint-set data structure
    group_by_node = {}
    for node in weight_by_edge.keys():
        group_by_node[node] = {node}

    # Loop through edges and add to minimum spanning tree if it doesn't create a cycle
    mst_edges = set()
    for edge, weight in edges:
        node1, node2 = edge
        if group_by_node[node1] != group_by_node[node2]:
            mst_edges.add(edge)
            group_by_node[node1] |= group_by_node[node2]
            group_by_node[node2] = group_by_node[node1]

    # Return set of edges in minimum spanning tree
    return mst_edges
```

Both programs take in a dictionary `weight_by_edge` representing an undirected graph, where the keys are pairs of nodes and the values are edge weights. They first sort the edges by weight and create a disjoint-set data structure to keep track of which nodes are connected. Then, the program loops through the edges and adds them to the minimum spanning tree if they don't create a cycle. Finally, the program returns the set of edges in the minimum spanning tree.