
from collections import defaultdict

def find_two_paths_with_same_xor_sum(t: int, test_cases: List[Tuple[int, int, int, List[Tuple[int, int, int]]]]) -> List[str]:
    results = []
    for i in range(t):
        n, a, b, edges = test_cases[i]
        graph = defaultdict(list)
        for edge in edges:
            u, v, w = edge
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        paths_from_a = bfs(graph, a, n)
        paths_from_b = bfs(graph, b, n)
        
        xor_sums = defaultdict(int)
        for node in range(1, n+1):
            for path in paths_from_a[node]:
                xor_sums[node] ^= path[1]
            for path in paths_from_b[node]:
                xor_sums[node] ^= path[1]
                
        if any(count > 1 for count in Counter(xor_sums.values()).values()):
            results.append('YES')
        else:
            results.append('NO')
    
    return results


def bfs(graph, start, n):
    paths = [[] for i in range(n + 1)]
    queue = [(start, [])]
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        node, path = queue.pop(0)
        
        paths[node].append((start, 0))
        for p in path:
            paths[node].append(p)
        
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, path + [(node, weight)]))
    
    return paths
