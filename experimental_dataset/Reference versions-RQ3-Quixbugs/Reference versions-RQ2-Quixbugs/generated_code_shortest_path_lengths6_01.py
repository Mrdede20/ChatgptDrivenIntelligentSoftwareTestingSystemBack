
def shortest_path_lengths(n, length_by_edge):
    shortest_paths = {}
    for i in range(n):
        for j in range(n):
            shortest_paths[(i,j)] = length_by_edge.get((i,j), float('inf'))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if shortest_paths[(i,j)] > shortest_paths[(i,k)] + shortest_paths[(k,j)]:
                    shortest_paths[(i,j)] = shortest_paths[(i,k)] + shortest_paths[(k,j)]
    return shortest_paths
