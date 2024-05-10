
from collections import deque

def topo_sort(nodes):
    # Calculate indegree for each node
    indegrees = {node: 0 for node in nodes}
    for node in nodes:
        for successor in node.successors:
            indegrees[successor] += 1

    # Add nodes with no incoming edges to the queue
    queue = deque([node for node in nodes if indegrees[node] == 0])
    ordered_nodes = []

    # Process nodes in the queue
    while queue:
        current_node = queue.popleft()
        ordered_nodes.append(current_node)

        for successor in current_node.successors:
            indegrees[successor] -= 1
            if indegrees[successor] == 0:
                queue.append(successor)

    # Check for cycles
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Graph contains cycles")

    return ordered_nodes
