
import heapq

class FibHeapNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

    def add_child(self, child):
        child.parent = self
        self.degree += 1
        if self.child == None:
            self.child = child.left = child.right = child
        else:
            child.left = self.child.left
            child.right = self.child
            self.child.left.right = child
            self.child.left = child

    def remove_child(self, child):
        child.parent = None
        self.degree -= 1
        if self.child == child:
            if child.left == child:
                self.child = None
            else:
                self.child = child.left
        child.left.right = child.right
        child.right.left = child.left

class FibHeap:
    def __init__(self):
        self.min_node = None
        self.nodes = {}

    def insert(self, key, val):
        new_node = FibHeapNode(key, val)
        self.nodes[key] = new_node
        if self.min_node == None:
            self.min_node = new_node
        else:
            self.min_node.right.left = new_node
            new_node.right = self.min_node.right
            self.min_node.right = new_node
            new_node.left = self.min_node
            if new_node.val < self.min_node.val:
                self.min_node = new_node

    def minimum(self):
        return self.min_node.val

    def extract_min(self):
        min_node = self.min_node
        if min_node != None:
            if min_node.child != None:
                child = min_node.child
                while child != min_node.child.left:
                    child.parent = None
                    child = child.right
                min_node.left.right = min_node.child
                min_node.child.left.right = min_node.right
                min_node.right.left = min_node.child.left
                min_node.child.left = min_node.left
            else:
                min_node.right.left = min_node.left
                min_node.left.right = min_node.right
            if min_node == min_node.right:
                self.min_node = None
            else:
                self.min_node = min_node.right
                self.consolidate()
            del self.nodes[min_node.key]
            return min_node.val

    def consolidate(self):
        degree_arr = [None] * 100
        node = self.min_node
        while True:
            degree = node.degree
            while degree_arr[degree] != None:
                other_node = degree_arr[degree]
                if node.val > other_node.val:
                    node, other_node = other_node, node
                node.add_child(other_node)
                degree_arr[degree] = None
                degree += 1
            degree_arr[degree] = node
            node = node.right
            if node == self.min_node:
                break
        self.min_node = None
        for node in degree_arr:
            if node != None:
                if self.min_node == None:
                    self.min_node = node
                else:
                    self.min_node.right.left = node.right
                    node.right.left = self.min_node
                    node.right = self.min_node.right
                    self.min_node.right = node
                    if node.val < self.min_node.val:
                        self.min_node = node

def insert_or_update(heap, key, val):
    if key in heap.nodes:
        node = heap.nodes[key]
        node.val = val
        while node.parent != None and node.val < node.parent.val:
            node.val, node.parent.val = node.parent.val, node.val
            node = node.parent
        if node.val < heap.min_node.val:
            heap.min_node = node
    else:
        heap.insert(key, val)

def get(heap, key):
    if key in heap.nodes:
        return heap.nodes[key].val
    else:
        return float('inf')

def dijkstra(length_by_edge, start, goal):
    heap = FibHeap()
    visited = set()
    insert_or_update(heap, start, 0)
    while heap.min_node != None:
        curr_node_key = heap.min_node.key
        curr_node_val = heap.extract_min()
        visited.add(curr_node_key)
        if curr_node_key == goal:
            return curr_node_val
        for succ in length_by_edge[curr_node_key]:
            if succ not in visited:
                new_dist = curr_node_val + length_by_edge[curr_node_key][succ]
                insert_or_update(heap, succ, new_dist)
    return float('inf')
