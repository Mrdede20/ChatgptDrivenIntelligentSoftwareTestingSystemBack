
from collections import defaultdict


def floyd_warshall(n, length_by_edge):
    # Create a defaultdict object to hold the shortest path lengths
    shortest_paths = defaultdict(lambda: defaultdict(lambda: float('inf')))
    
    # Set the initial distances between nodes
    for node, edges in length_by_edge.items():
        for neighbor, distance in edges.items():
            shortest_paths[node][neighbor] = distance
            
    # Iterate through every node and update shortest path lengths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if shortest_paths[i][j] > shortest_paths[i][k] + shortest_paths[k][j]:
                    shortest_paths[i][j] = shortest_paths[i][k] + shortest_paths[k][j]
    
    # Return the dictionary of shortest path lengths
    return shortest_paths
