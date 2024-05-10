
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
