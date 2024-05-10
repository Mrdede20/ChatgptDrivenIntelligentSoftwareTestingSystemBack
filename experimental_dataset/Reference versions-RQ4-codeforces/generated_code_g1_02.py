
def find_same_xor_paths(adj_list: list, A: int, B: int) -> bool:
    # Convert adjacency list to undirected graph
    graph = [[] for _ in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            graph[i].append(neighbor)
            graph[neighbor].append(i)
    
    # Use BFS to find all paths from A to B and store their XOR sums
    paths = []
    queue = [(A, 0, [])]
    while queue:
        node, xor_sum, current_path = queue.pop(0)
        if node == B:
            paths.append(xor_sum)
        else:
            for neighbor in graph[node]:
                if neighbor not in current_path:
                    queue.append((neighbor, xor_sum ^ 1, current_path + [node]))
    
    # Check if there exist two XOR sums that are the same
    for i in range(len(paths)):
        for j in range(i+1, len(paths)):
            if paths[i] == paths[j]:
                return True
                
    return False
