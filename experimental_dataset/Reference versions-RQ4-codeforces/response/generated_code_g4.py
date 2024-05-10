Here are two versions of the program that achieve the same intention:

Version 1:

```
def check_distance_odd_or_even(T: int, tests: list) -> None:
    """
    Given T test cases, checks if the distance d between two nodes A and B is odd or even.
    """
    for i in range(T):
        n = tests[i][0]
        a = tests[i][1]
        b = tests[i][2]
        d = tests[i][3]
        graph = {}
        for j in range(n-1):
            u, v, w = tests[i][4+j]
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))
            graph[v].append((u, w))
        q = []
        q.append(a)
        visited = [False]*(n+1)
        level = [0]*(n+1)
        visited[a] = True
        while len(q)!=0:
            current = q.pop(0)
            for neighbor, weight in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    level[neighbor] = level[current] + 1
                    q.append(neighbor)
        if level[b]!=0 and level[b]%2==0 and d%2==0:
            print("YES")
        elif level[b]!=0 and level[b]%2!=0 and d%2!=0:
            print("YES")
        else:
            print("NO")
```

In this version, we use a dictionary to store the graph, where each node has a list of its neighbors and their corresponding weights. We then perform a Breadth-First Search (BFS) starting from node A to find the level (distance) of node B from node A. We then check if the distance d between A and B is odd or even, and print "YES" if the parity of the distance matches the parity of the level, and "NO" otherwise. 

Version 2:

```
from collections import defaultdict

def check_distance_odd_or_even(T: int, tests: list) -> None:
    """
    Given T test cases, checks if the distance d between two nodes A and B is odd or even.
    """
    def dfs(v, p=-1):
        """
        Performs a DFS on the graph, starting at vertex v.
        """
        nonlocal dist, graph
        for u in graph[v]:
            if u != p:
                dist[u] = dist[v] + graph[v][u]
                dfs(u, v)

    for i in range(T):
        n = tests[i][0]
        a = tests[i][1]
        b = tests[i][2]
        d = tests[i][3]
        graph = defaultdict(dict)
        for j in range(n-1):
            u, v, w = tests[i][4+j]
            graph[u][v] = w
            graph[v][u] = w
        dist = [0]*n
        dfs(a)
        if dist[b]%2==0 and d%2==0:
            print("YES")
        elif dist[b]%2!=0 and d%2!=0:
            print("YES")
        else:
            print("NO")
```

In this version, we use a defaultdict of dictionaries to store the graph, where each node has a dictionary of its neighbors and their corresponding weights. We then perform a Depth-First Search (DFS) starting from node A to find the distance (sum of weights along the path) between node A and all other nodes. We then check if the distance d between A and B is odd or even, and print "YES" if the parity of the distance matches the parity of the distance between A and B, and "NO" otherwise. Note that we use nested functions in this version to allow us to use a nonlocal variable, dist, to store the distances.