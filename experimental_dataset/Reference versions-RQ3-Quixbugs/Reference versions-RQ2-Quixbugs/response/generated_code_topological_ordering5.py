Program 1:

```
from collections import deque

def topological_sort(nodes):
    ordered_nodes = []
    no_incoming_nodes = deque([node for node in nodes if not node.incoming_nodes])
    
    while no_incoming_nodes:
        node = no_incoming_nodes.popleft()
        ordered_nodes.append(node)
        
        for outgoing_node in node.outgoing_nodes:
            outgoing_node.incoming_nodes.remove(node)
            if not outgoing_node.incoming_nodes:
                no_incoming_nodes.append(outgoing_node)
    
    if len(ordered_nodes) != len(nodes):
        raise ValueError("Graph contains a cycle")
    
    return ordered_nodes
```

Program 2:

```
def topological_sort(nodes):
    visited = set()
    ordering = []
    
    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        
        for outgoing_node in node.outgoing_nodes:
            dfs(outgoing_node)
            
        ordering.append(node)
    
    for node in nodes:
        dfs(node)
    
    ordering.reverse()
    
    if len(ordering) != len(nodes):
        raise ValueError("Graph contains a cycle")
    
    return ordering
```

Both programs implement the topological sorting algorithm using the same method name "topological_sort" and the same parameter type "nodes", which is a list of directed graph nodes. The first program uses a deque to keep track of nodes with no incoming edges, while the second program uses a depth-first search approach starting from each node to find the ordering. Both programs raise a ValueError if the graph contains a cycle.