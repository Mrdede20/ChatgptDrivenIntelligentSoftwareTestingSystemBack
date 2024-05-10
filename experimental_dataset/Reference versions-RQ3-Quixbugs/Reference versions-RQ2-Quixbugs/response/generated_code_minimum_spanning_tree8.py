Sure, here's one way to implement Kruskal's algorithm in Python:
```python
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
```
Here's another way to implement Kruskal's algorithm using the `networkx` library:
```python
import networkx as nx

def kruskal(graph):
    # Create a graph using 'networkx' library and add all nodes
    G = nx.Graph()
    nodes = set()
    for edge in graph:
        node1, node2 = edge
        nodes.add(node1)
        nodes.add(node2)
        G.add_edge(node1, node2, weight=graph[edge])
    
    # Run Kruskal's algorithm on the graph
    mst = nx.minimum_spanning_tree(G)
    
    # Extract the set of edges from the minimum spanning tree
    edges = set((edge[0], edge[1]) for edge in mst.edges())
    
    # Return the set of edges in the MST
    return edges
```
Both programs implement Kruskal's algorithm to find the Minimum Spanning Tree of an undirected graph. The first program does so by defining the functions `find` and `union` to detect and avoid cycles, while the second program uses the `networkx` library to build and manipulate the graph.