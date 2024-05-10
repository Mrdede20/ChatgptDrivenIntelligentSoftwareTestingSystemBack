 
def kruskal(edges):
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

    result = set()
    parent = {}
    rank = {}

    for edge in edges:
        parent[edge[0]] = edge[0]
        parent[edge[1]] = edge[1]
        rank[edge[0]] = 0
        rank[edge[1]] = 0

    edges = sorted(edges, key=lambda x: x[2])

    for edge in edges:
        u = edge[0]
        v = edge[1]

        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.add((u, v, edge[2]))
            union(parent, rank, u, v)

    return result
