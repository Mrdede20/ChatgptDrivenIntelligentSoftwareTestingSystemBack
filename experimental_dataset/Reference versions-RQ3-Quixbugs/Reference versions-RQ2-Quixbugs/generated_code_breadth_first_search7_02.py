
def bfs_search(start_node, goal_node):
    queue = [start_node]
    distances = {start_node: 0}

    while queue:
        node = queue.pop(0)
        if node == goal_node:
            return True
        for successor in node.successors:
            if successor not in distances:
                distances[successor] = distances[node] + 1
                queue.append(successor)
    
    return False
