
class DepthFirstSearch:
    def __init__(self, start_node, goal_node):
        self.visited = set()
        self.start_node = start_node
        self.goal_node = goal_node

    def dfs(self, current_node):
        if current_node == self.goal_node:
            return True
        if current_node in self.visited:
            return False
        self.visited.add(current_node)
        for successor in current_node.successors:
            if self.dfs(successor):
                return True
        return False

    def search(self):
        return self.dfs(self.start_node)
