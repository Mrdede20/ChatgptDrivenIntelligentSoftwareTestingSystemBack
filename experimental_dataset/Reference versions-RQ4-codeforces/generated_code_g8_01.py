
from collections import defaultdict, deque


def search_nodes(graph, start, end):
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return visited
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist+1))
    return set()


def solution(graph, a, b):
    nodes_a_to_b = search_nodes(graph, a, b)
    nodes_b_to_a = search_nodes(graph, b, a)
    common_nodes = nodes_a_to_b.intersection(nodes_b_to_a)
    if len(common_nodes) >= 2 or len(nodes_b_to_a) > 2:
        return True
    return False

