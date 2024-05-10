
from collections import defaultdict
 
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.edges = defaultdict(list)
 
    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))
         
    def bellman_ford(self, src):
 
        dist = defaultdict(lambda: float('inf'))
        dist[src] = 0
 
        for i in range(self.V - 1):
            for u in self.edges:
                for v, w in self.edges[u]:
                    if dist[u] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
 
        for u in self.edges:
            for v, w in self.edges[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    return "Graph contains negative weight cycle"
                     
        return dict(dist)
