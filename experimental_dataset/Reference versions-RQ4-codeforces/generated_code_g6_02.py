
from collections import deque
from typing import List, Tuple

def evaluate_tree(n: int, a: int, b: int, edges: List[Tuple[int,int]]) -> str:
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    def bfs(start):
        distance = [-1] * n
        queue = deque([start])
        distance[start] = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[node] ^ 1
                    queue.append(neighbor)
        return distance

    distance_a = bfs(a-1)
    distance_b = bfs(b-1)

    for i in range(n):
        if distance_a[i] % 2 == distance_b[i] % 2 == 0:
            return "YES"
    
    return "NO"
