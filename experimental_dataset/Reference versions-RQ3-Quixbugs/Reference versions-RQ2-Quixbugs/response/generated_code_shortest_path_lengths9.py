Here are two programs that implement the Floyd-Warshal algorithm:

Program 1:

```python
from collections import defaultdict

def floyd_warshal(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    for i in range(n):
        length_by_path[(i, i)] = 0
    for u, v in length_by_edge.keys():
        length_by_path[(u, v)] = length_by_edge[(u, v)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[(i, j)] = min(length_by_path[(i, j)], length_by_path[(i, k)] + length_by_path[(k, j)])
    return dict(length_by_path)
```

Program 2:

```python
from collections import defaultdict

def floyd_warshal(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    for u, v in length_by_edge.keys():
        length_by_path[(u, v)] = length_by_edge[(u, v)]
    for i in range(n):
        length_by_path[(i, i)] = 0
        for j in range(i+1, n):
            for k in range(i+1, j):
                if length_by_path[(i, j)] > length_by_path[(i, k)] + length_by_path[(k, j)]:
                    length_by_path[(i, j)] = length_by_path[(i, k)] + length_by_path[(k, j)]
                    length_by_path[(j, i)] = length_by_path[(i, j)]
    return dict(length_by_path)
```

Both programs take in two arguments, `n` and `length_by_edge`, and return a dictionary containing the shortest path length keyed by the ordered pair of node ids.

The first program uses three nested for loops to iterate over all node pairs and calculate the shortest path connecting each ordered pair of nodes in the graph. The second program is a slightly modified version of the first program that only iterates over node pairs once using two nested for loops and an if statement to update the shortest path.

Both programs use the defaultdict function from the collections module to assign a lambda function that returns float('inf') as the default value for the length_by_path, and also to initialize the diagonal entries to 0.