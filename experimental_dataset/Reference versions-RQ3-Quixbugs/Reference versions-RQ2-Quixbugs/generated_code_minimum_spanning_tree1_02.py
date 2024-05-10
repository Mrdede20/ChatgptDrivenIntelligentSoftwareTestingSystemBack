
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
