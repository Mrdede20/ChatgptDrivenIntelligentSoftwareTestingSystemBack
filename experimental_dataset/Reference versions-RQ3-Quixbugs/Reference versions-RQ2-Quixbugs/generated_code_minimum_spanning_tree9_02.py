
class KruskalsAlgorithm:
    
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
    
    def kruskals_algorithm(self, weight_by_edge):
        self.parent = {node: node for node in weight_by_edge.keys()}
        self.rank = {node: 0 for node in weight_by_edge.keys()}
        edges = list(weight_by_edge.items())
        edges.sort(key=lambda x:x[1])
        mst = set()
        for edge, weight in edges:
            node1, node2 = edge
            if self.find(node1) != self.find(node2):
                self.union(node1, node2)
                mst.add((min(node1, node2), max(node1, node2)))
        return mst
