
from collections import deque

class Node:
    def __init__(self, value=None, successors=[]):
        self.value = value
        self.successors = successors

def bfs(start_node, goal_node):
    queue = deque([start_node])
    visited = set()
    
    while queue:
        current_node = queue.popleft()
        if current_node == goal_node:
            return True
        
        visited.add(current_node)
        
        for neighbor_node in current_node.successors:
            if neighbor_node not in visited:
                queue.append(neighbor_node)
    return False
