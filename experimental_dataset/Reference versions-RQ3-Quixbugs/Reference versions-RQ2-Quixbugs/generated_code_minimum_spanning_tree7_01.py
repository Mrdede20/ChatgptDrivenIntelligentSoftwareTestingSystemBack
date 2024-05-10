
def kruskal(weight_by_edge):
    edges = sorted(weight_by_edge.keys(), key=lambda x: weight_by_edge[x]) # sort edges by weight
    group_by_node = {node: [node] for node in weight_by_edge.keys()} # initialize each node in its own group
    mst = set() # initialize empty set of edges

    for edge in edges:
        node1, node2 = edge
        group1, group2 = group_by_node[node1], group_by_node[node2]
        if group1 != group2: # if nodes not in the same group (i.e. edge does not create cycle)
            mst.add(edge) # add edge to the minimum spanning tree
            group = group1 + group2 # merge groups
            for node in group:
                group_by_node[node] = group # update group_by_node
    return mst
