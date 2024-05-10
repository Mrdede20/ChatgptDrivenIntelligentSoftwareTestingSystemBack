Sure, here are two implementations of the Bellman-Ford algorithm:

Implementation 1:

```
from collections import defaultdict
 
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
         
    def bellman_ford(self, src):
 
        dist = defaultdict(lambda: float('inf'))
        dist[src] = 0
 
        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
 
        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return "Graph contains negative weight cycle"
                     
        return dict(dist)
```

Implementation 2:

```
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
```

Both implementations take in a graph object and a source node as parameters, and return a dictionary that maps each node in the graph to the minimum weight of a path from the source node. The first implementation uses a list of edges to define the graph, while the second uses a dictionary with nodes as keys and their outgoing edges as values.