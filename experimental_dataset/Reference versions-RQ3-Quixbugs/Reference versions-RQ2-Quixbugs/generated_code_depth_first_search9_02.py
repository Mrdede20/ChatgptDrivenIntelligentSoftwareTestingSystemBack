
def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        nodesvisited.add(node)
        if node == goalnode:
            return True
        for successor in node.successors:
            if search_from(successor):
                return True
        return False

    return search_from(startnode)
