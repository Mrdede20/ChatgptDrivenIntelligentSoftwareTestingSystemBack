
from collections import defaultdict, deque

def binary_bfs(n:int, a:int, b:int, nodes:list) -> str:
    # Construct the graph
    graph = defaultdict(list)
    for i in range(n):
        x, y, w = nodes[i]
        graph[x].append((y, w))
        graph[y].append((x, w))
        
    # Helper function for binary BFS
    def bfs(start:int, target:int) -> tuple:
        queue = deque()
        queue.append(start)
        visited = set([start])
        prev = [-1] * (n+1)
        prev[start] = -2
        cost = [0] * (n+1)
        while queue:
            curr = queue.popleft()
            for neig, weight in graph[curr]:
                if neig not in visited:
                    visited.add(neig)
                    queue.append(neig)
                    prev[neig] = curr
                    cost[neig] = cost[curr] ^ weight
                    if neig == target:
                        return prev, cost
        return None, None
    
    # Perform binary BFS from both a and b
    prev_a, cost_a = bfs(a, b)
    prev_b, cost_b = bfs(b, a)
    
    # Check if there is more than one common node or if the target has more than two zero weight paths
    for i in range(1, n+1):
        if i != a and i != b and prev_a[i] != -1 and prev_b[i] != -1:
            if cost_a[i] ^ cost_b[i] == 0:
                return "YES"
    
    for i in range(1, n+1):
        if i != a and i != b and prev_a[i] != -1 and prev_b[i] != -1 and cost_a[i] == 0 and cost_b[i] == 0:
            return "YES"
    
    return "NO"
