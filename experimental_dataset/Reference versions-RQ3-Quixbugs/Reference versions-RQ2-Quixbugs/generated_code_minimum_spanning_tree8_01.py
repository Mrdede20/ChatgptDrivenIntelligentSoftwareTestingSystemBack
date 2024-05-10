
def kruskal(graph):
    # Initialize the parent dictionary, rank dictionary, and edge set
    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}
    edges = set()

    # Define functions to find the parent of a node and to union two sets
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

    # Sort the graph edges by weight
    sorted_edges = sorted(graph.keys(), key=lambda x: graph[x])

    # Iterate through the edges and add them to the MST if they don't create a cycle
    for edge in sorted_edges:
        weight = graph[edge]
        node1, node2 = edge[0], edge[1]
        if find(node1) != find(node2):
            union(node1, node2)
            edges.add(edge)

    # Return the set of edges in the MST
    return edges
