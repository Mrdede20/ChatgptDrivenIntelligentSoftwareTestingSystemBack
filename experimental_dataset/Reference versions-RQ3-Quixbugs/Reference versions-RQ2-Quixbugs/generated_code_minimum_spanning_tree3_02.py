
def minimum_spanning_tree(weight_by_edge):
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

    def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    edges = sorted(weight_by_edge.keys(), key=lambda x: weight_by_edge[x])
    parent = {}
    rank = {}
    for edge in edges:
        node1, node2 = edge
        if node1 not in parent:
            parent[node1] = node1
            rank[node1] = 0
        if node2 not in parent:
            parent[node2] = node2
            rank[node2] = 0
        x = find(parent, node1)
        y = find(parent, node2)
        if x != y:
            union(parent, rank, x, y)
            mst.add(edge)

    return set(mst)
