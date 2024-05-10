
from collections import defaultdict, deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited


def solution(graph, a, b):
    nodes_a_to_b = bfs(graph, a)
    nodes_b_to_a = bfs(graph, b)
    common_nodes = nodes_a_to_b.intersection(nodes_b_to_a)
    if len(common_nodes) >= 2 or len(nodes_b_to_a) > 2:
        return True
    return False

