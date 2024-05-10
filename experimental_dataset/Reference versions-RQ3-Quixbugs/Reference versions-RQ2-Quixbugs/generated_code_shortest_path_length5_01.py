
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
