
def depth_first_search(start_node, goal_node):
    
    def search_from(current_node, visited):
        visited.add(current_node)
        
        if current_node == goal_node:
            return True
        
        for successor in current_node.successors:
            if successor not in visited:
                if search_from(successor, visited):
                    return True
        
        return False
    
    nodesvisited = set()
    return search_from(start_node, nodesvisited)
