
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
