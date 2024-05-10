
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
