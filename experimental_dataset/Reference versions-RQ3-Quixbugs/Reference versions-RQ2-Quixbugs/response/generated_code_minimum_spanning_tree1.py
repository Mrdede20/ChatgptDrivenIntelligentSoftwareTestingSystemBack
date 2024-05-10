Program 1:

```
def kruskal_mst(edge_weights):
    """
    This function takes in a dictionary of edge weights representing an undirected connected weighted graph and
    returns the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm.
    """
    edges = sorted(edge_weights.keys(), key=lambda x: edge_weights[x])
    parent = {vertex: vertex for vertex in set(sum(edges, ()))}
    mst = []

    def find(parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent, parent[vertex])
        return parent[vertex]

    def union(parent, rank, vertex1, vertex2):
        if rank[vertex1] < rank[vertex2]:
            parent[vertex1] = vertex2
        elif rank[vertex1] > rank[vertex2]:
            parent[vertex2] = vertex1
        else:
            parent[vertex2] = vertex1
            rank[vertex1] += 1

    rank = {vertex: 0 for vertex in parent}
    for edge in edges:
        vertex1, vertex2 = edge
        root1, root2 = find(parent, vertex1), find(parent, vertex2)
        if root1 != root2:
            mst.append(edge)
            union(parent, rank, root1, root2)

    return mst
```

Program 2:

```
from heapq import heappush, heappop


def kruskal_mst(edge_weights):
    """
    This function takes in a dictionary of edge weights representing an undirected connected weighted graph and
    returns the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm.
    """
    edges = sorted(edge_weights.items(), key=lambda x: x[1])
    parent = {vertex: vertex for vertex in edge_weights.keys()}
    mst = []

    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(vertex1, vertex2):
        root1, root2 = find(vertex1), find(vertex2)
        if root1 != root2:
            parent[root2] = root1

    for edge, weight in edges:
        vertex1, vertex2 = edge
        if find(vertex1) != find(vertex2):
            mst.append(edge)
            union(vertex1, vertex2)

    return mst
```

Both of these programs implement Kruskal's algorithm to find the Minimum Spanning Tree (MST) of an undirected connected weighted graph. The first program uses a union-find data structure to ensure that no cycles are formed while adding edges to the MST. The second program uses a heap data structure to efficiently add edges of increasing weight to the MST while ensuring that no cycles are formed.