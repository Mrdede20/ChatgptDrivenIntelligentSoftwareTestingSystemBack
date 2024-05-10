Sure, here are two programs:

Program 1:

``` python
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
```

Program 2:

``` python
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
``` 

Both programs use the same method name `kruskal(edges)` and the same parameter type `edges`, which is a dictionary of edges and their corresponding weights. The implementations differ slightly in terms of the internal functions used for finding and merging sets, but both use the same approach of sorting the edges by weight and checking for cycles using the disjoint-set data structure.