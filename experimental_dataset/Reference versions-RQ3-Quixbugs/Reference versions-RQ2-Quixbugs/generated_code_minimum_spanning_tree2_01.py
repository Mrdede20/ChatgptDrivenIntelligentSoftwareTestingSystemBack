 
def kruskal(edges):
    def find(parent, node):
        if parent[node] != node:
            parent[node] = find(parent, parent[node])
        return parent[node]

    def union(parent, rank, u, v):
        uroot, vroot = find(parent, u), find(parent, v)
        if rank[uroot] < rank[vroot]:
            parent[uroot] = vroot
        elif rank[vroot] < rank[uroot]:
            parent[vroot] = uroot
        else:
            parent[vroot] = uroot
            rank[uroot] += 1

    parent = {node: node for node in edges.keys()}
    rank = {node: 0 for node in edges.keys()}
    sortedEdges = sorted(edges.items(), key=lambda x: x[1])
    result = set()

    for edge, weight in sortedEdges:
        u, v = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            result.add((u, v, weight))

    return result
