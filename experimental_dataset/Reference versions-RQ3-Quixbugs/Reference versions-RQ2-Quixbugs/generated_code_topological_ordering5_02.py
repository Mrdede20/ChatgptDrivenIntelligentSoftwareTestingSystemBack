
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
