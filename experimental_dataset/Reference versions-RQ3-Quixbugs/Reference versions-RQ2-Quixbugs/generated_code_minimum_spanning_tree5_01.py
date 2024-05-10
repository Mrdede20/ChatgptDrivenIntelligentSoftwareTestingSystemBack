
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
