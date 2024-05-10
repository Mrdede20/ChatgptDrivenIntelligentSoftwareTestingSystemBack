Program 1:

```
import sys
import math
from collections import defaultdict
from fibheap import *

class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

def dijkstra(graph, startnode, goalnode):
    dist = defaultdict(lambda: math.inf)
    prev = {}
    unvisited_nodes = makefheap()

    dist[startnode] = 0
    unvisited_nodes.add((startnode, 0))

    while len(unvisited_nodes):
        node, _ = unvisited_nodes.extract_min()

        if node == goalnode:
            path = []
            while node in prev:
                path.append(node)
                node = prev[node]
            path.append(startnode)

            return list(reversed(path))

        for neighbor in graph[node]:
            alt = dist[node] + graph[node][neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = node
                unvisited_nodes.add_or_update((neighbor, alt))

    return None
```

Program 2:

```
import sys
import math
from collections import defaultdict
from queue import PriorityQueue

class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

def dijkstra(graph, startnode, goalnode):
    dist = defaultdict(lambda: math.inf)
    prev = {}
    visited_nodes = set()
    unvisited_nodes = PriorityQueue()

    dist[startnode] = 0
    unvisited_nodes.put((0, startnode))

    while not unvisited_nodes.empty():
        _, node = unvisited_nodes.get()

        if node == goalnode:
            path = []
            while node in prev:
                path.append(node)
                node = prev[node]
            path.append(startnode)

            return list(reversed(path))

        visited_nodes.add(node)

        for neighbor in graph[node]:
            if neighbor in visited_nodes:
                continue

            alt = dist[node] + graph[node][neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = node
                unvisited_nodes.put((alt, neighbor))

    return None
``` 

Both programs implement Dijkstra's algorithm with the given Node class as the input parameter. The first program uses a Fibonacci heap while the second program uses a priority queue to store unvisited nodes.