
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
