
def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        nodesvisited.add(node)
        if node == goalnode:
            return True
        return any(search_from(successor) for successor in node.successors)

    return search_from(startnode)
