Option 1:
```
import heapq

class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

def dijkstra(graph, source, target):
    heap = [(0, source)]
    visited = set()
    while heap:
        (cost, current_node) = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == target:
            return cost
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor))
    return float('inf')

def get(heap, node):
    for (cost, n) in heap:
        if n == node:
            return cost
    return None

def insert_or_update(heap, node, cost):
    if node in [n for (c, n) in heap]:
        heap.remove((get(heap, node), node))
    heapq.heappush(heap, (cost, node))
    
length_by_edge = {('A', 'B'): 2, ('A', 'C'): 5, ('B', 'C'): 1, ('B', 'D'): 6, ('C', 'D'): 3}
graph = {}
for n1, n2 in length_by_edge:
    if n1 not in graph:
        graph[n1] = {n2: length_by_edge[(n1, n2)]}
    else:
        graph[n1][n2] = length_by_edge[(n1, n2)]
    if n2 not in graph:
        graph[n2] = {n1: length_by_edge[(n1, n2)]}
    else:
        graph[n2][n1] = length_by_edge[(n1, n2)]

print(dijkstra(graph, 'A', 'D'))
```

Option 2:
```
import heapq

class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

def dijkstra(length_by_edge, start, goal):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, current_node) = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            return cost
        for neighbor, weight in length_by_edge[(current_node,)].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor))
    return float('inf')

def get(heap, node):
    for (cost, n) in heap:
        if n == node:
            return cost
    return None

def insert_or_update(heap, node, cost):
    if node in [n for (c, n) in heap]:
        heap.remove((get(heap, node), node))
    heapq.heappush(heap, (cost, node))

length_by_edge = {('A', 'B'): 2, ('A', 'C'): 5, ('B', 'C'): 1, ('B', 'D'): 6, ('C', 'D'): 3}
graph = {}
for n1, n2 in length_by_edge:
    if n1 not in graph:
        graph[n1] = {}
    graph[n1][n2] = length_by_edge[(n1, n2)]

print(dijkstra(graph, 'A', 'D'))