Sure! Here are two programs that achieve the given intention using Kruskal's algorithm:

Program 1:

```
def kruskalsAlgorithm(graph):
    result = set()
    vertices = set()
    disjointSet = {}

    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])

    for vertex in vertices:
        disjointSet[vertex] = vertex

    sortedGraph = sorted(graph, key=graph.get)

    for edge in sortedGraph:
        parent1 = find(disjointSet, edge[0])
        parent2 = find(disjointSet, edge[1])

        if parent1 != parent2:
            result.add(edge)
            disjointSet[parent1] = parent2

    return result

def find(disjointSet, vertex):
    if disjointSet[vertex] != vertex:
        disjointSet[vertex] = find(disjointSet, disjointSet[vertex])
    return disjointSet[vertex]
```

Program 2:

```
from collections import defaultdict

def kruskalsAlgorithm(graph):
    result = set()
    vertices = set()
    disjointSet = {}

    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])

    for vertex in vertices:
        disjointSet[vertex] = vertex

    sortedGraph = sorted(graph, key=graph.get)

    for edge in sortedGraph:
        parent1 = find(disjointSet, edge[0])
        parent2 = find(disjointSet, edge[1])

        if parent1 != parent2:
            result.add(edge)
            disjointSet[parent1] = parent2

    return result

def find(disjointSet, vertex):
    if disjointSet[vertex] != vertex:
        disjointSet[vertex] = find(disjointSet, disjointSet[vertex])
    return disjointSet[vertex]
```
Both programs have the same method name, parameter type, and use Kruskal's algorithm for finding the Minimum Spanning Tree of a given weighted undirected graph using Union-Find Algorithm. The input is a dictionary with edges as keys and their corresponding weights as values, representing the weight of each edge. The output is a set of edges that connect all the vertices of the input graph and has the least possible total weight.