
def reverse_linked_list(node):
    if not node or not node.successor:
        return node
    new_head = reverse_linked_list(node.successor)
    node.successor.successor = node
    node.successor = None
    return new_head
