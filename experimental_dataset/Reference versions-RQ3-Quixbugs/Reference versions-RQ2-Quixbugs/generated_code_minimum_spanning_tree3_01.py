
def minimum_spanning_tree(weight_by_edge):
    edges = sorted(weight_by_edge.keys(), key=lambda x: weight_by_edge[x])
    parent = {node: node for node in weight_by_edge.keys()}
    rank = {node: 0 for node in weight_by_edge.keys()}
    mst = set()

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    for edge in edges:
        node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            mst.add(edge)

    return mst
