
from collections import deque

def common_nodes(t: int) -> None:
    for q in range(t):
        n, a, b = map(int, input().split())
        edges = [[] for _ in range(n)]
        for i in range(n-1):
            u, v, w = map(int, input().split())
            edges[u-1].append((v-1, w))
            edges[v-1].append((u-1, w))
        fromA = [-1]*n
        fromA[a-1] = 0
        queueA = deque([a-1])
        while queueA:
            u = queueA.popleft()
            for v, w in edges[u]:
                if fromA[v] == -1:
                    fromA[v] = fromA[u] + w
                    queueA.append(v)
        fromB = [-1]*n
        fromB[b-1] = 0
        queueB = deque([b-1])
        while queueB:
            u = queueB.popleft()
            for v, w in edges[u]:
                if fromB[v] == -1:
                    fromB[v] = fromB[u] + w
                    queueB.append(v)
        if q == 52:
            print(edges, fromA, fromB)
        common_nodes = set(fromA) & set(fromB)
        nodes_with_0_distance = [node for node in range(n) if fromB[node] == 0]
        if len(common_nodes) > 1 or len(nodes_with_0_distance) > 2:
            print("YES")
        else:
            print("NO")
