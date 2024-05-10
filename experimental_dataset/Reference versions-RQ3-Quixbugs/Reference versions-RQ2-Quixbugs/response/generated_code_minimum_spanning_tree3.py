Program 1:

```
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
```

Program 2:

```
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
```

Both of these programs implement Kruskal's algorithm to find the Minimum Spanning Tree (MST) for an undirected connected graph using the same function name and parameter type. The first program makes use of the path compression and union by rank optimization techniques to improve the performance of the algorithm, while the second program uses a recursive function to find the parent of each node and performs union operations based on the rank of the parent nodes.