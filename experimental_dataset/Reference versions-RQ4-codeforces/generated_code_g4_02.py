
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
