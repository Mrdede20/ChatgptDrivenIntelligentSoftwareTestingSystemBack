Here are two Python programs for implementing Kruskal's algorithm to find the minimum spanning tree of an input graph:

Program 1:

```python
def kruskal_mst(graph):
    # Create a list of edges sorted by increasing weight
    edges = sorted(graph.items(), key=lambda x: x[1])
    
    # Create a dictionary to keep track of which nodes belong to which set
    nodes = {}
    
    # Create a list to store the minimum spanning tree
    mst = []
    
    # Start with each node in its own set
    for edge in edges:
        node1, node2 = edge[0]
        weight = edge[1]
        
        # If nodes are not in the same set, add the edge to the minimum spanning tree
        if nodes.get(node1, node1) != nodes.get(node2, node2):
            mst.append(edge)
            old_set = nodes.get(node1, node1)
            new_set = nodes.get(node2, node2)
            
            # Merge the two sets
            for node in nodes:
                if nodes[node] == old_set:
                    nodes[node] = new_set

    return mst
```

Program 2:

```python
def kruskal_mst(graph):
    # Create a list of edges sorted by increasing weight
    edges = sorted(graph.items(), key=lambda x: x[1])
    
    # Create a list to store the minimum spanning tree
    mst = []
    
    # Create a dictionary to track which nodes are in which component
    nodes = {n: i for i, n in enumerate(set().union(*graph.keys()))}
    components = list(range(len(nodes)))
    
    # Iterate over each edge and add it to the tree if it doesn't create a cycle
    for edge in edges:
        (u, v), weight = edge
        if components[u] != components[v]:
            mst.append(edge)
            new_component = components[u]
            old_component = components[v]
            for i, c in enumerate(components):
                if c == old_component:
                    components[i] = new_component
                    
    return mst
```

Both programs use the same method name `kruskal_mst` and the same parameter type, which is a dictionary where the keys are pairs of nodes representing edges of the graph, and the values are the weights assigned to each edge. They also have the same time complexity of O(E log E), where E is the number of edges in the input graph.