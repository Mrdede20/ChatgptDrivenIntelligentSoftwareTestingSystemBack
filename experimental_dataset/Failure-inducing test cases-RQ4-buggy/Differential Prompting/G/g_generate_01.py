import sys
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
import threading

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
        queue = deque([(a, 0)])
        visited_a = {a: 0}
        while queue:
            node, xor_val = queue.popleft()
            for neighbor, weight in graph[node]:
                if neighbor not in visited_a:
                    visited_a[neighbor] = xor_val ^ weight
                    queue.append((neighbor, xor_val ^ weight))
        queue = deque([(b, 0)])
        visited_b = {b: 0}
        while queue:
            node, xor_val = queue.popleft()
            for neighbor, weight in graph[node]:
                if neighbor not in visited_b:
                    visited_b[neighbor] = xor_val ^ weight
                    queue.append((neighbor, xor_val ^ weight))
        pos = False
        for val in visited_a.values():
            if val in visited_b.values():
                pos = True
                break
        if pos:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

# Alternative way to start the main function as a separate thread
# threading.Thread(target=main).start()
