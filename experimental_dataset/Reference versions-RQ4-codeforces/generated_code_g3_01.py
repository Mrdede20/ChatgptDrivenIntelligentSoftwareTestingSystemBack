
from collections import deque

def two_paths(t: int, n: int, a: int, b: int, edges: list) -> None:
    for _ in range(t):
        # Create adjacency list
        adj_list = [[] for _ in range(n+1)]
        for i in range(n-1):
            u, v, w = map(int, input().split())
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        
        # Breadth First Search from vertex a
        visited = [False] * (n+1)
        visited[a] = True
        fromA = [0] * (n+1)
        queue = deque([(a, 0)])
        while queue:
            x, path = queue.popleft()
            fromA[x] = path
            for y, weight in adj_list[x]:
                if not visited[y]:
                    visited[y] = True
                    queue.append((y, path^weight))

        # Breadth First Search from vertex b
        visited = [False] * (n+1)
        visited[b] = True
        fromB = [0] * (n+1)
        queue = deque([(b, 0)])
        while queue:
            x, path = queue.popleft()
            fromB[x] = path
            for y, weight in adj_list[x]:
                if not visited[y]:
                    visited[y] = True
                    queue.append((y, path^weight))

        # Check if there are two different paths between a and b
        if any([(fromA[x] ^ fromB[x]) > 0 for x in range(1, n+1)]):
            print("YES")
        # Check if there is a vertex reachable more than twice from b
        elif fromB.count(0) > 2:
            print("YES")
        else:
            print("NO")
