
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
