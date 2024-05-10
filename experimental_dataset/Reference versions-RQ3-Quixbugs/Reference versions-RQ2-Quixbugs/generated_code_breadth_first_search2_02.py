
from queue import Queue

class Node:
    def __init__(self, value=None, successors=[]):
        self.value = value
        self.successors = successors

def bfs(start_node, goal_node):
    queue = Queue(maxsize=0)
    queue.put(start_node)
    visited = set()
    
    while not queue.empty():
        current_node = queue.get()
        if current_node == goal_node:
            return True
        
        visited.add(current_node)
        
        for neighbor_node in current_node.successors:
            if neighbor_node not in visited:
                queue.put(neighbor_node)
    return False
