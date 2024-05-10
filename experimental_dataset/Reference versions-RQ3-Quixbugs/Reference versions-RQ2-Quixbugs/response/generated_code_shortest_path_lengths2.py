Program 1:

```
from collections import defaultdict

def floyd_warshall(num_nodes, edges):
    shortest_paths = defaultdict(lambda: float('inf'))

    for i in range(1, num_nodes+1):
        shortest_paths[(i,i)] = 0

    for edge, weight in edges.items():
        shortest_paths[edge] = weight

    for k in range(1, num_nodes+1):
        for i in range(1, num_nodes+1):
            for j in range(1, num_nodes+1):
                shortest_paths[(i,j)] = min(shortest_paths[(i,j)], shortest_paths[(i,k)]+shortest_paths[(k,j)])

    return shortest_paths
```

Program 2:

```
from collections import defaultdict

def floyd_warshall(num_nodes, edges):
    shortest_paths = defaultdict(lambda: float('inf'))

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                shortest_paths[(i, j)] = 0
            elif (i, j) in edges:
                shortest_paths[(i, j)] = edges[(i, j)]

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                shortest_paths[(i, j)] = min(shortest_paths[(i, j)], shortest_paths[(i, k)] + shortest_paths[(k, j)])
       
    return shortest_paths
```

Both programs take in the same input parameters:

- `num_nodes`: an integer representing the number of nodes in the graph
- `edges`: a dictionary of edge lengths keyed by an ordered pair of node ids

Both programs output a dictionary containing the shortest path length keyed by an ordered pair of node ids.

The main difference between the two programs is in the way the initial graph is constructed. In the first program, the graph is initialized with the length of each edge between nodes, while in the second program, the graph is initialized with a default value of infinity and then updated with edge lengths if they exist in the input dictionary.

Both programs use a triple-nested loop to implement the Floyd-Warshall algorithm to find the length of the shortest path connecting every ordered pair of nodes in a directed graph. The first loop considers all possible intermediate nodes, the second loop considers the starting nodes, and the innermost loop considers the ending nodes.