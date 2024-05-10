
from collections import deque

class Node:
    def __init__(self, value=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def is_reachable(self, start_node, goal_node):
        queue = deque([start_node])
        seen = set([start_node])

        while queue:
            current_node = queue.popleft()
            if current_node == goal_node:
                return True
            for successor in current_node.successors:
                if successor not in seen:
                    seen.add(successor)
                    queue.append(successor)
        return False
