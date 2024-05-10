
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
