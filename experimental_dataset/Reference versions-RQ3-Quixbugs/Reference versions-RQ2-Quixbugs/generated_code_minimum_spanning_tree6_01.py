
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
