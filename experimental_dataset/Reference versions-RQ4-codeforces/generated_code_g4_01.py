
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
