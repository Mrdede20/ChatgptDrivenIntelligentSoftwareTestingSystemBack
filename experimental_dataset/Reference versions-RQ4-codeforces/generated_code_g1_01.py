
def find_same_xor_paths(adj_list: list, A: int, B: int) -> bool:
    # Convert adjacency list to undirected graph
    graph = [[] for _ in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            graph[i].append(neighbor)
            graph[neighbor].append(i)
    
    # Use DFS to find all paths from A to B and store their XOR sums
    paths = []
    def dfs(node, target, visited, xor_sum, current_path):
        if node == target:
            paths.append(xor_sum)
        else:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, target, visited, xor_sum ^ 1, current_path + [neighbor])
            visited.remove(node)
    
    dfs(A, B, set(), 0, [])
    
    # Check if there exist two XOR sums that are the same
    for i in range(len(paths)):
        for j in range(i+1, len(paths)):
            if paths[i] == paths[j]:
                return True
                
    return False
