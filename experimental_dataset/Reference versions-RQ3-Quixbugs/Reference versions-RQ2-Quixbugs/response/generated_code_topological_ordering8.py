Method 1:

```
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
```

Method 2:

```
def topo_sort(nodes):
    # Create empty list to store the sorted nodes
    sorted_nodes = []
    
    # Create a set of nodes with no incoming edges
    root_nodes = set()
    for node in nodes:
        if not node.predecessors:
            root_nodes.add(node)
            
    # Traverse the graph
    while root_nodes:
        current_node = root_nodes.pop()
        sorted_nodes.append(current_node)

        for successor in current_node.successors:
            # Remove current_node from its successor's predecessors
            successor.predecessors.remove(current_node)

            # Add successor to the set of root nodes if it has no more predecessors
            if not successor.predecessors:
                root_nodes.add(successor)

    # Check for cycles
    if len(sorted_nodes) != len(nodes):
        raise ValueError("Graph contains cycles")

    return sorted_nodes
``` 

Both of these methods take in a list of nodes representing the input graph and return an ordered list of nodes. The first method uses a deque-based approach while the second method uses a set-based approach. They both check for cycles and raise a ValueError if the input graph contains cycles.