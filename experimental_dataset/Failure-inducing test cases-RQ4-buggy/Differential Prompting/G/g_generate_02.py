import sys
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify

def ri():
    return int(input().strip())

def rs():
    return input().strip()

def rl():
    return list(map(int, input().split()))

def rls():
    return input().split()

def main():
    test = ri()
    for _ in range(test):
        n, a, b = rl()
        graph = defaultdict(list)
        for i in range(n-1):
            u, v, w = rl()
            graph[u].append((v, w))
            graph[v].append((u, w))
        q = deque([(a, 0)])
        visited_a = set([a])
        while q:
            node, xor = q.popleft()
            for neighbor, weight in graph[node]:
                if neighbor not in visited_a:
                    visited_a.add(neighbor)
                    q.append((neighbor, xor^weight))
        q = deque([(b, 0)])
        visited_b = set([b])
        pos = False
        while q:
            node, xor = q.popleft()
            if xor in visited_a:
                pos = True
                break
            for neighbor, weight in graph[node]:
                if neighbor not in visited_b:
                    visited_b.add(neighbor)
                    q.append((neighbor, xor^weight))
        if pos:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
    # Alternatively, run the main function in a separate thread
    # import threading
    # threading.Thread(target=main).start()
